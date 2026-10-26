# Normas de Código

## Nombrado

* Los identificadores, comentarios y textos de la interfaz se escriben en español (ej. `crearViaje`, `obtenerVotacion`). Se mantienen en inglés solo los nombres impuestos por librerías o frameworks.
* Las clases, los tipos y los componentes de React deben ir en PascalCase (ej. `UsuarioController`, `MisViajes`). Los ficheros de componentes y pantallas se llaman igual que su componente (ej. `MisViajes.tsx`).
* Las variables, funciones y métodos deben ir en camelCase (ej. `calcularTotal`, `idGasto`). Los ficheros de servicios y utilidades también (ej. `viajesApi.ts`, `viajeService.js`).
* Las constantes deben ir en mayúsculas separadas por guiones bajos (ej. `MAX_REINTENTOS`).
* Claridad y longitud: los nombres deben ser autoexplicativos. Queda prohibido usar variables de una sola letra (como x, a, aux), excepto para índices de bucles muy cortos (como i).

## Estructura

* Se respeta la estructura de carpetas de cada repositorio. No se crean carpetas nuevas si ya hay una para ese tipo de fichero.
  * Frontend: `screens` (pantallas), `components` (piezas reutilizables), `services` (llamadas a la API), `utils` (funciones puras), `router` y `styles`.
  * Backend: `routes` → `controllers` (valida la entrada y elige la respuesta HTTP) → `services` (acceso a Supabase), y `middleware`.
* Una función hace una sola cosa. La lógica que se necesita en dos sitios se extrae a una función compartida en lugar de copiarla.
* Los colores, tipografías y medidas de la interfaz salen de los tokens de `styles/tokens.ts`, no se escriben a mano en cada pantalla.

## Limpieza y validación

* El código debe compilar sin mostrar ningún warning (TypeScript y linter).
* No debe haber importaciones (imports) que no se estén utilizando.
* Nada de código comentado: no se debe dejar código comentado por el típico "por si acaso luego hace falta". Para recuperar código antiguo ya usamos Git.
* Sin rastros de depuración: prohibido subir `console.log`, `System.out.print` o funciones similares de prueba. Solo se permiten los mensajes de registro del servidor que informan de su funcionamiento (arranque, conexiones, errores).
* Variables sin leer: no debe haber variables declaradas a las que luego nunca se les da uso.
* Comentarios: explican el porqué de lo que no es evidente, no repiten lo que ya dice el código.
* Formato e indentación unificados: todo el equipo usa exactamente la misma configuración, **2 espacios** (prohibido mezclar espacios y tabuladores). Para que sea automático, se recomienda configurar el editor para que "formatee al guardar".
* Manejo de errores: queda prohibido dejar bloques de excepciones (catch) vacíos. Si se captura un error, se trata: se responde con el error correspondiente, se muestra un mensaje al usuario o se deja un registro claro de lo que ha fallado.
* Dependencias: no se añade una librería nueva sin comentarlo antes con el equipo. Se elige una mantenida y con licencia libre.
