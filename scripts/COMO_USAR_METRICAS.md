# Métricas del sprint: cómo funcionan

Las gráficas de **burndown** (horas estimadas que quedan) y **burnup** (puntos de historia hechos)
de cada sprint se generan solas a partir de las issues. Se actualizan al crear, editar, cerrar,
reabrir o cambiar de milestone una issue, y cada noche a las 23:50.

## Convenciones

| Qué | Dónde | Ejemplo |
|---|---|---|
| Sprint | Milestone de la PBI (`S2`, `S3`, `S4`) | La fecha del milestone es el último día del sprint |
| Puntos de historia | Línea en el cuerpo de la **PBI** | `Puntos de historia: 5` |
| Horas estimadas | Línea en el cuerpo de cada **tarea** | `Estimación: 2,5 h` |
| PBI sin tareas | Lleva su propia `Estimación` | `Estimación: 4,5 h` |
| Hecho | Cerrar la issue | La PBI la cierra la PO al aceptarla |
| Fuera del sprint | Cerrar como *Not planned* | Sale del alcance |

Las tareas se reconocen por el título (`PB-16.1.2 ...`) y pertenecen al sprint de su PBI.
En el README aparece un aviso con las issues a las que les falte la estimación o los puntos.

## Inicio de cada sprint (planificación)

1. Asignar el milestone a las PBIs del sprint y poner sus `Puntos de historia`.
2. Crear las tareas con su `Estimación`.
3. Durante los **2 primeros días** del sprint el compromiso (inicio de la línea ideal) se ajusta solo:
   podéis añadir tareas y re-estimar sin que cuente como cambio de alcance.

A partir del tercer día, añadir una tarea o subir una estimación hace que la curva **suba** ese día
(es lo correcto en Scrum). Los días anteriores nunca se modifican.

## Las horas son estimadas, no reales

Si una tarea se estimó en 4 h y costó 8, el burndown baja 4 al cerrarla. No apuntéis horas reales aquí.

## Ajustes manuales (Actions → «Métricas Scrum» → Run workflow)

- **recomprometer = S3**: fija el inicio de la línea ideal al total de horas actual (si la planificación se alargó).
- **reiniciar = S3**: borra el histórico de ese sprint y lo reconstruye con las fechas de cierre
  (pierde los cambios de alcance registrados; solo para arreglar errores).

## Recomendación

Cerrad cada tarea el mismo día que la terminéis: la gráfica usa la fecha de cierre.
