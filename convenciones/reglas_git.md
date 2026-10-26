# Normas de Git

## Commits

* Cada commit contiene un único cambio lógico, que compila y no rompe las pruebas. Una PBI grande se divide en varios commits (por ejemplo, base de datos, backend y pantalla).
* El mensaje se escribe en español:
  * El asunto empieza en mayúscula, no termina en punto, tiene un máximo de 72 caracteres y al menos 3 palabras.
  * El asunto describe qué hace el cambio (ej. «Pantalla Votaciones: votar, ver resultados y cerrar votación»).
  * Si el commit es grande (cambia muchos ficheros o la razón no es evidente), se añade un cuerpo, separado por una línea en blanco, que explica qué cambia y por qué.
* No se suben ficheros generados por herramientas locales, dependencias (`node_modules`), resultados de pruebas ni ficheros `.env`.

## Integración en main

* Antes de subir: `git pull` para integrar los cambios del resto del equipo, resolver los conflictos y volver a pasar las pruebas.
* No se sube a `main` código que no compile o con pruebas en rojo. Si la CI falla después de subir, arreglarla es lo primero.
* No se reescribe la historia de `main` (`push --force`) salvo acuerdo de todo el equipo, y solo con `--force-with-lease`.

## Issues

* Cada PBI tiene su issue en GitHub, con sus criterios de satisfacción, pantalla del prototipo, horas estimadas y puntos de historia.
