# Definición de hecho

Un elemento del Product Backlog (PBI) se considera **Hecho**, y su issue se puede cerrar, solo cuando cumple todos los criterios de la tabla. La tabla dice qué se exige; cada enlace lleva al detalle y a cómo se comprueba.

| Criterio | Se cumple cuando... | Detalle |
| --- | --- | --- |
| **Criterios de satisfacción** | Se cumplen todos los criterios de satisfacción de la PBI, cada uno cubierto por al menos una prueba de aceptación o E2E, y se ha mostrado funcionando al resto del equipo. | [Estrategia de pruebas](calidad/estrategia_de_pruebas.md#pruebas-de-aceptación) |
| **Revisión de código** | Otra persona del equipo ha revisado el código con la lista de comprobación, y no quedan comentarios bloqueantes sin resolver. | [Revisión de código](calidad/revision_de_codigo.md) |
| **Convenciones** | El código sigue las normas de código, de API, de base de datos y de Git del proyecto. | [Código](convenciones/reglas_codigo.md) · [API](convenciones/reglas_API.md) · [Base de datos](convenciones/reglas_base_de_datos.md) · [Git](convenciones/reglas_git.md) |
| **Calidad estática** | El proyecto compila sin errores ni warnings (TypeScript, linter) y el Quality Gate de SonarCloud está en verde, sin bugs ni vulnerabilidades nuevos. | [Revisión de código](calidad/revision_de_codigo.md#calidad-estática) |
| **Pruebas automatizadas (RNF)** | Hay pruebas nuevas en los niveles que pide la PBI (unitarias, de integración, E2E, de aceptación), todas las pruebas pasan en local y en la CI, y cada bug corregido tiene su prueba de regresión. | [Estrategia de pruebas](calidad/estrategia_de_pruebas.md) |
| **Integración continua** | El cambio está integrado en `main` de cada repositorio afectado y su pipeline de CI termina en verde. | [Git](convenciones/reglas_git.md#integración-en-main) |
| **Seguridad y privacidad (RNF)** | Conexiones HTTPS/WSS, endpoints protegidos por sesión, datos de entrada validados en el backend, tablas nuevas con RLS y sin secretos en el repositorio. | [Seguridad](convenciones/reglas_seguridad.md) |
| **Usabilidad y accesibilidad (RNF)** | Las pantallas nuevas o modificadas se ven bien entre 320 y 430 px de ancho, sin scroll horizontal, con estados de error visibles y controles con nombre accesible. | [Diseño móvil](convenciones/reglas_responsive_movil.md) |
| **Documentación** | Los endpoints nuevos o modificados están en el contrato OpenAPI y en la colección de Postman. Los cambios de base de datos están en los scripts SQL. La documentación generada está al día. | [API](convenciones/reglas_API.md#documentación) · [Base de datos](convenciones/reglas_base_de_datos.md) |
| **Despliegue** | La funcionalidad pasa la prueba de humo en un móvil Android real y, si hay cambios de base de datos, los scripts están aplicados en Supabase. | [Prueba de humo](calidad/prueba_de_humo.md) |

## Aplicación

- **Quién la comprueba:** la persona autora rellena la lista y quien revisa el código la confirma. La issue solo la cierra quien revisa.
- **Criterios que no aplican:** si un criterio no tiene sentido para una PBI (por ejemplo, Documentación en una PBI solo de interfaz), no se aplica. No se puede saltar un criterio solo por falta de tiempo.
- **Si no se cumple:** la PBI no está hecha y no cuenta como completada en el sprint. La issue vuelve a «En curso» con la lista de lo que falta.
- **Revisión de la definición:** se revisa en la retrospectiva de cada sprint. Los cambios se acuerdan en la reunión, quedan en el acta y se aplican a las PBIs que empiecen después.
