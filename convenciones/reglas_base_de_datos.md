# Normas de base de datos

## Scripts

* La base de datos se define solo con los scripts SQL del backend: `scripts/01_create_tables.sql` (tipos, tablas e índices) y `scripts/02_politicas_rls.sql` (funciones auxiliares, RLS, políticas y funciones). No se crean ni modifican tablas a mano desde el panel de Supabase sin reflejarlo en los scripts.
* Los scripts se pueden ejecutar varias veces sin error y sin duplicar datos: `CREATE TABLE IF NOT EXISTS`, tipos dentro de bloques `DO` que comprueban si existen, `DROP POLICY IF EXISTS` antes de cada política y `CREATE OR REPLACE FUNCTION`.
* Si un cambio afecta a datos que ya existen (por ejemplo, una columna nueva obligatoria), el script incluye también la actualización de esos datos, que tampoco se repite si se ejecuta dos veces.
* Al terminar la PBI, los scripts modificados se aplican en Supabase, y en la issue se indica que están aplicados.

## Diseño

* Tablas y columnas en español y en `snake_case`. Las tablas en plural (ej. `viajes`, `opciones_votacion`).
* Toda tabla tiene clave primaria `id uuid` (o una clave compuesta si es una tabla de relación) y, si procede, `creado_en timestamptz`.
* Las claves foráneas indican qué pasa al borrar (`ON DELETE CASCADE` o `SET NULL`), para no dejar datos huérfanos.
* Las reglas que deben cumplirse siempre se ponen en la base de datos (`NOT NULL`, `CHECK`, `UNIQUE`), además de validarse en el backend.
* Se crean índices para las columnas por las que se filtra a menudo (claves foráneas, búsquedas).
* La seguridad de cada tabla sigue las [normas de seguridad](reglas_seguridad.md#datos).

## Documentación

* Cada tabla, columna no evidente, política y función lleva un comentario `--` justo encima, que explica para qué sirve.
* Esos comentarios generan `Backend/docs/BASE_DE_DATOS.md` con `npm run docs`, y la CI comprueba con `npm run docs:check` que el documento está al día.
