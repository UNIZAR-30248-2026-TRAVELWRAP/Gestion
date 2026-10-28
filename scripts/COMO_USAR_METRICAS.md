# Diagramas de burndown y burnup

En esta carpeta guardamos el **burndown** (horas estimadas que nos quedan) y el **burnup**
(puntos de historia que hemos completado) de cada sprint. Los genera una GitHub Action a partir
de nuestras issues: se actualizan cada vez que creamos, editamos, cerramos, reabrimos o cambiamos
de milestone una issue, y además cada noche a las 23:50. Medimos desde el Sprint 2.

## Nuestras convenciones

| Qué | Dónde lo indicamos | Ejemplo |
|---|---|---|
| Sprint | Milestone de la PBI (`S2`, `S3`, `S4`) | La fecha del milestone es el último día del sprint |
| Puntos de historia | Línea en el cuerpo de la **PBI** | `Puntos de historia: 5` |
| Horas estimadas | Línea en el cuerpo de cada **tarea** | `Estimación: 2,5 h` |
| PBI sin tareas | La propia PBI lleva su `Estimación` | `Estimación: 4,5 h` |
| Hecho | Cerramos la issue | El desarrollador cierra la PBI cuando cumple la DoD |
| Fuera del sprint | La cerramos como *Not planned* | Sale del alcance |

Las tareas se identifican por el título (`PB-16.1.2 ...`) y cuentan en el sprint de su PBI.
Si a alguna issue le falta la estimación o los puntos, aparece en el README como pendiente.

## Al empezar cada sprint

1. Asignamos el milestone a las PBIs del sprint y les ponemos sus `Puntos de historia`.
2. Creamos las tareas con su `Estimación`.
3. Durante los **2 primeros días** el compromiso (punto de partida de la línea ideal) se ajusta
   solo, así que podemos añadir tareas y re-estimar sin que cuente como cambio de alcance.

A partir del tercer día, si añadimos una tarea o subimos una estimación, la curva **sube** ese día.
Los días anteriores no se modifican nunca.

## Durante el sprint

- Cerramos cada tarea el mismo día que la terminamos, porque el diagrama usa la fecha de cierre.
- Las horas son **estimadas**, no reales: si una tarea estimada en 4 h nos lleva 8, el burndown
  baja 4 al cerrarla. Aquí no registramos horas reales.

## Ajustes manuales

Desde *Actions → Métricas Scrum → Run workflow*:

- **recomprometer = S3**: fija el inicio de la línea ideal en el total de horas actual
  (por si la planificación se alarga más de dos días).
- **reiniciar = S3**: borra el histórico de ese sprint y lo reconstruye con las fechas de cierre.
  Se pierden los cambios de alcance registrados, así que lo reservamos para corregir errores.

## Archivos

- `burndown_SX.png` y `burnup_SX.png`: diagramas de cada sprint.
- `historico.json`: foto diaria del estado de cada sprint (no lo editamos a mano).