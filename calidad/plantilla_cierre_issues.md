# Plantillas para cerrar issues

Comentarios para copiar en GitHub al cerrar una issue. Hay dos:

- [Sub-issue](#1-sub-issue): cada tarea de GUI, Backend, Documentación o Testing.
- [Issue de la PBI](#2-issue-de-la-pbi): la entrada de pila que agrupa sus sub-issues.

Cómo rellenarlas:

- Cambia lo que va entre `< >` y borra lo que no aplique.
- Los commits se enlazan con el formato largo, porque las issues están en el repositorio Gestion y el código en Backend o Frontend: `UNIZAR-30248-2026-TRAVELWRAP/Backend@<hash>` o `UNIZAR-30248-2026-TRAVELWRAP/Frontend@<hash>`. El hash corto se copia en GitHub Desktop (History → botón derecho sobre el commit → Copy SHA).
- Las fechas de cierre alimentan los diagramas de burndown y burnup: cierra cada issue el día que se termina, no todas al final del sprint.

## 1. Sub-issue

Se cierra cuando su commit está en `main` y la CI de ese repositorio termina en verde.

```markdown
Hecho.

<Qué se ha hecho, en una a tres líneas o viñetas.>

Commits: UNIZAR-30248-2026-TRAVELWRAP/<Backend|Frontend>@<hash>
```

Qué contar según la etiqueta de la sub-issue:

| Etiqueta | Qué explicar |
| --- | --- |
| **GUI** | Qué pantalla es, qué muestra, qué valida y adónde lleva al terminar |
| **Backend** | El endpoint (`MÉTODO /api/...`), qué recibe y devuelve, quién puede usarlo y, si hay tablas nuevas, su RLS |
| **Documentación** | Las operaciones añadidas al contrato OpenAPI (`docs/API.md` regenerado) y los casos de la colección de Postman |
| **Testing** | Las pruebas nuevas del backend y del frontend: unitarias, E2E con Playwright y aceptación con Cucumber (nombre del `.feature`) |

## 2. Issue de la PBI

Se cierra cuando todas sus sub-issues están cerradas y se cumple la [definición de hecho](../definicion_de_hecho.md).

```markdown
## Completado

**Criterio de satisfacción:** «<copiado literal de la hoja del plan>»
- [x] <Qué puede hacer el usuario>
- [x] <Qué se ve o se recalcula>
- [x] <Restricciones: solo miembros, solo con el viaje activo...>

**Definición de hecho**
- [x] Criterios de satisfacción cubiertos por pruebas de aceptación o E2E y mostrados al equipo
- [x] Convenciones de código, API, base de datos y Git
- [x] Compila sin errores ni warnings y el Quality Gate de SonarCloud está en verde
- [x] Pruebas nuevas en los niveles que pide la PBI, en verde en local y en la CI
- [x] Integrado en `main` de cada repositorio afectado, con la CI en verde
- [x] Seguridad: endpoints con sesión, validación en el backend, RLS en tablas nuevas y sin secretos
- [x] Pantallas correctas entre 320 y 430 px, con errores visibles y controles con nombre accesible
- [x] OpenAPI, Postman, scripts SQL y documentación generada al día
- [x] Prueba de humo en un Android real y scripts SQL aplicados en Supabase

Criterios que no aplican: <ninguno | cuáles y por qué>

Subtareas: #<GUI>, #<Backend>, #<Documentación>, #<Testing>.
```
