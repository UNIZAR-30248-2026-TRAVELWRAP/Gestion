# Normas de la API

## Diseño de las rutas

* Todas las rutas cuelgan de `/api` y usan sustantivos en plural, nunca verbos (ej. `/api/viajes` en lugar de `/api/getViajes`).
* Los recursos que pertenecen a otro se anidan bajo él (ej. `/api/viajes/{viajeId}/votaciones/{votacionId}`).
* Los identificadores de las rutas son UUID. Si un identificador no tiene formato UUID, se responde 400 sin consultar la base de datos.
* Las acciones que no encajan en crear, leer, modificar o borrar se modelan como un subrecurso con `POST` y un verbo en infinitivo (ej. `POST /viajes/{viajeId}/archivar`, `POST /votaciones/{votacionId}/cerrar`). Es la única excepción a la regla de no usar verbos.

## Métodos HTTP

| Método | Uso | Respuesta correcta |
| --- | --- | --- |
| `GET` | Consultar. Nunca modifica datos. | 200 |
| `POST` | Crear un recurso o ejecutar una acción. | 201 si crea, 200 si es una acción |
| `PUT` | Crear o sustituir un recurso entero cuya ruta ya se conoce (ej. el voto del usuario). | 200 |
| `PATCH` | Modificar solo los campos que se envían. | 200 |
| `DELETE` | Borrar. | 204 sin cuerpo, o 200 si devuelve el recurso actualizado |

## Formato

* La entrada y la salida de datos son siempre JSON. Los campos van en `snake_case`, igual que las columnas de la base de datos (ej. `fecha_inicio`).
* El backend valida y limpia todos los datos de entrada (tipos, longitudes, formatos, valores permitidos) antes de usarlos. No confía en las validaciones del frontend.
* Los errores tienen siempre la misma estructura, con un código estable que el frontend puede comprobar y un mensaje en español para mostrar al usuario:

  ```json
  { "error": { "codigo": "viaje_no_encontrado", "mensaje": "El viaje no existe o no perteneces a él" } }
  ```

* Los mensajes de error no revelan detalles internos (consultas SQL, trazas, nombres de tablas).

## Códigos de estado

| Código | Cuándo |
| --- | --- |
| 400 | Datos de entrada no válidos (`datos_invalidos` u otro código más concreto) |
| 401 | Sin sesión o con sesión caducada (`sin_sesion`, `sesion_invalida`) |
| 403 | Con sesión, pero sin permiso para la acción (ej. `no_creador`) |
| 404 | El recurso no existe o el usuario no tiene acceso a él (las políticas RLS no permiten distinguirlo) |
| 409 | La acción choca con el estado actual (ej. `viaje_no_activo`, `votacion_cerrada`, `opcion_duplicada`) |
| 500 | Error interno no previsto del servidor (`error_interno`) |
| 502 | Error al comunicarse con Supabase |

## Documentación

Cada endpoint nuevo o modificado se documenta en el mismo cambio que lo implementa:

* **OpenAPI 3.0** (`Backend/docs/openapi.yaml`), con:
  * Ruta: la URL exacta (ej. `/viajes/{viajeId}`).
  * Tipo: el método HTTP correspondiente.
  * Seguridad: si necesita el token de sesión.
  * Entrada (Request): parámetros y JSON que recibe, con un ejemplo.
  * Salida (Response): qué devuelve en cada código de estado posible, con un ejemplo de cada error.
* **Postman** (`Backend/docs/TravelWrap.postman_collection.json`): al menos una petición del caso correcto y una por cada error que pueda provocar el usuario, con sus `pm.test`.
* **Documentación generada:** después de cambiar el contrato se ejecuta `npm run docs`, que actualiza `Backend/docs/API.md` y `Backend/docs/BASE_DE_DATOS.md`. La CI comprueba con `npm run docs:check` que están al día.
