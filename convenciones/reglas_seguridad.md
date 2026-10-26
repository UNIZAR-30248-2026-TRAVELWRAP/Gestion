# Seguridad y privacidad

## Conexiones y autenticación

* Todas las conexiones fuera del entorno local usan HTTPS y WSS.
* La autenticación la gestiona Supabase: con email y contraseña o con Google OAuth. El backend no guarda contraseñas.
* Todo endpoint que lee o modifica datos de un usuario exige sesión (middleware `requiereSesion`), salvo los de autenticación.
* El backend accede a Supabase con el token del usuario (`req.supabase`), para que se apliquen las políticas RLS. La clave de servicio, que se salta RLS, no se usa para atender peticiones de usuarios.

## Datos

* Toda tabla nueva tiene RLS activado y una política para cada operación que se permita (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). Lo que no tiene política queda prohibido.
* Un usuario solo ve los datos de los viajes de los que es miembro. Las acciones reservadas al creador del viaje se comprueban también en la base de datos, no solo en la interfaz.
* Las funciones SQL son `SECURITY INVOKER` salvo que necesiten saltarse RLS por un motivo concreto, que se explica en su comentario. Las `SECURITY DEFINER` fijan `search_path` y solo las puede ejecutar el rol `authenticated`.
* El backend valida todos los datos de entrada (ver [normas de la API](reglas_API.md#formato)).
* Las respuestas solo incluyen los datos que necesita la pantalla. No se devuelven emails ni datos personales de otros usuarios si no hacen falta.

## Secretos

* Las claves y contraseñas van en ficheros `.env`, que no se suben al repositorio (están en `.gitignore`). En la CI se guardan como secretos de GitHub.
* Si se sube un secreto por error, se cambia (rotar la clave en Supabase o Google) aunque después se borre del repositorio.
* No se copian secretos ni datos personales en issues, actas, capturas o mensajes de error.

## Comprobación

* La revisión de código revisa estos puntos ([lista de comprobación](../calidad/revision_de_codigo.md#seguridad-y-datos)).
* Las políticas RLS nuevas se prueban: un miembro puede, quien no es miembro no puede, y las acciones del creador fallan para el resto ([estrategia de pruebas](../calidad/estrategia_de_pruebas.md)).
* SonarCloud no debe mostrar vulnerabilidades ni *security hotspots* nuevos sin revisar.
