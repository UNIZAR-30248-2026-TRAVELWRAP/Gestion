# Estrategia de pruebas

No se busca probar cada detalle, sino que las funciones clave de cada PBI estén probadas en **varios niveles**, de forma que un fallo se detecte en el nivel más barato posible.

## Niveles

| Nivel | Qué prueba | Herramienta y ubicación | Obligatorio en |
| --- | --- | --- | --- |
| **Unitarias** | Funciones, validaciones, componentes y pantallas aisladas, con la red simulada. | Frontend: Vitest y Testing Library en `tests_unit/`. Backend: `node --test` en `test/`. | Toda PBI con lógica nueva |
| **Integración (backend)** | Controlador y servicio juntos, con un cliente de Supabase simulado: códigos HTTP, formato de las respuestas y de los errores. | `node --test` en `test/` | Todo endpoint nuevo o modificado |
| **E2E** | El flujo principal de la PBI en el navegador, con la API simulada. | Playwright en `tests/` (Chromium, Firefox y WebKit) | Toda PBI con interfaz |
| **Aceptación** | Los criterios de satisfacción de la PBI escritos como escenarios. | Cucumber en `tests_cucumber/features/` (un fichero `pbXX_nombre.feature` por PBI) | Toda PBI con criterios de satisfacción |

## Qué se exige en cada PBI

- **Caso correcto y casos de error:** como mínimo, el flujo principal y los errores que el usuario puede provocar: datos no válidos, sin permiso, recurso inexistente, sin conexión...
- **Regresión:** cada bug corregido lleva una prueba que fallaba antes de la corrección.
- **Todas en verde:** antes de integrar en `main` pasan todas las pruebas del repositorio, no solo las nuevas. Una prueba no se borra ni se desactiva para que la CI pase. Si una prueba es inestable, se arregla o se abre una issue para arreglarla.
- **Pruebas independientes:** no dependen del orden de ejecución, de datos reales de Supabase ni de servicios externos (Google, red). Lo externo se simula.
- **Nombres descriptivos:** el nombre de la prueba dice el comportamiento esperado, por ejemplo «solo el creador del viaje puede cerrar la votación».

## Pruebas de aceptación

- Cada criterio de satisfacción de la PBI se corresponde con al menos un escenario de Cucumber o, si no es práctico, con una prueba E2E que lo indique en su nombre.
- Los escenarios se escriben en español, con el vocabulario del usuario y no con detalles técnicos.
- Además de las pruebas automáticas, la funcionalidad se muestra al resto del equipo (en la reunión semanal o en la revisión del sprint) antes de darla por hecha.

## Comandos

| Repositorio | Comando | Qué ejecuta |
| --- | --- | --- |
| Frontend | `npm test` | Pruebas unitarias (Vitest) |
| Frontend | `npm run test:e2e` | Pruebas E2E (Playwright) |
| Frontend | `npm run test:acceptance` | Pruebas de aceptación (Cucumber) |
| Backend | `npm test` | Pruebas unitarias y de integración |
