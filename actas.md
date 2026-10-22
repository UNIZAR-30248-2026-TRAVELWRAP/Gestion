# Actas de reuniones semanales

**Proyecto:** Travelwrap  
**Periodicidad:** miércoles, de 19:00 a 20:00  
**Participantes:** Daniel Blasco Labarta Berta Castillo Crespo y Adriana Sainz Sampedro  

## Calendario

| Fecha | Hito de referencia |
| --- | --- |
| [5 de octubre de 2026](#acta-2026-10-05) | Seguimiento de S1 (práctica 2, entrega el 22 de octubre) |
| [21 de octubre de 2026](#acta-2026-10-21) | Revisión final de S1 (entrega el 22 de octubre) |
| [28 de octubre de 2026](#acta-2026-10-28) | Seguimiento de S2 (práctica 3, entrega el 5 de noviembre) |
| [4 de noviembre de 2026](#acta-2026-11-04) | Revisión final de S2 (entrega el 5 de noviembre) |
| [11 de noviembre de 2026](#acta-2026-11-11) | Seguimiento de S3 (práctica 4, entrega el 19 de noviembre) |
| [18 de noviembre de 2026](#acta-2026-11-18) | Revisión final de S3 (entrega el 19 de noviembre) |
| [25 de noviembre de 2026](#acta-2026-11-25) | Seguimiento de S4 (práctica 5, entrega el 3 de diciembre) |
| [2 de diciembre de 2026](#acta-2026-12-02) | Revisión final de S4 (entrega el 3 de diciembre) |
| [9 de diciembre de 2026](#acta-2026-12-09) | Cierre y retrospectiva de S4 |

## Plantilla de cada reunión

Copiar esta sección para añadir reuniones posteriores al calendario. En cada reunión, actualizar los apartados de dedicación, riesgos, requisitos, issues y objetivos.

### [Fecha] — 19:00–20:00
  
**Ausencias y justificación:**  
**Hito o sprint en seguimiento:**  

#### Orden del día

1. Asuntos de trámite.
2. Revisión de la dedicación semanal.
3. Monitorización de riesgos.
4. Seguimiento de requisitos e issues completadas y pendientes.
5. Marcaje de objetivos para la semana siguiente.

#### 1. Asuntos de trámite

- **Temas tratados:**
- **Decisiones:**

#### 2. Dedicación semanal

| Integrante | Dedicación prevista (h) | Dedicación realizada (h) | Desviaciones / comentarios |
| --- | ---: | ---: | --- |
| Adriana Sainz Sampedro |  |  |  |
| Berta Castillo Crespo |  |  |  |
| Daniel Blasco Labarta |  |  |  |

#### 3. Riesgos

| Riesgo | Probabilidad / impacto | Estado y medidas |
| --- | --- | --- |
|  |  |  |

#### 4. Requisitos e issues

- **Requisitos completados:**
- **Requisitos pendientes o bloqueados:**
- **Issues completadas:**
- **Issues pendientes o bloqueadas:**
- **Bloqueos o dependencias:**

#### 5. Objetivos para la semana siguiente

| Objetivo / tarea | Responsable | Fecha objetivo |
| --- | --- | --- |
|  |  |  |

#### Acuerdos y cierre

- **Acuerdos:**
- **Próxima reunión:** miércoles, [fecha], de 19:00 a 20:00.

---

## Actas

<a id="acta-2026-10-05"></a>
### Lunes, 5 de octubre de 2026 — 19:00–20:00

**Asistentes:** Adriana Sainz Sampedro, Berta Castillo Crespo y Daniel Blasco Labarta
**Ausencias y justificación:** ninguna.
**Hito:** Seguimiento de S1 — práctica 2 (inicio del sprint; entrega: 22 de octubre)

#### Orden del día

1. Asuntos de trámite.
2. Revisión de la dedicación semanal.
3. Monitorización de riesgos.
4. Seguimiento de requisitos e issues completadas y pendientes.
5. Marcaje de objetivos para la semana siguiente.

#### 1. Asuntos de trámite

- **Temas tratados:**
  - Arranque del Sprint 1 (del 5 al 21 de octubre). Objetivo del sprint: prototipo refinado, entorno listo y acceso a la app con gestión básica de viajes.
  - Se recuerdan las herramientas del proyecto: PWA en React + TypeScript, Supabase (base de datos, autenticación y RLS), backend en Express con Socket.io, GitHub (repositorios Backend, Frontend y Gestion, e issues para el seguimiento), integración continua con GitHub Actions y SonarQube, pruebas con Cucumber y Playwright, y Figma Make para el prototipo.
  - Adriana avisa de que estará fuera una semana durante el sprint y de que tiene otros compromisos académicos y de trabajo, por lo que no podrá entregar sus tareas hasta el día 22, se le deja mayoritariamente frontend paraque no haya dependencias.
- **Decisiones:**
  - Se planifican menos horas para Adriana que para el resto del equipo y sus tareas se concentran al final del sprint.

#### 2. Dedicación semanal

| Integrante | Dedicación prevista (h) | Dedicación realizada (h) | Desviaciones / comentarios |
| --- | ---: | ---: | --- |
| Adriana Sainz Sampedro | 10 | — | Carga reducida por su ausencia; entrega de sus tareas hasta el 22 de octubre |
| Berta Castillo Crespo | 27 | — | Inicio del sprint |
| Daniel Blasco Labarta | 27 | — | Inicio del sprint |

#### 3. Riesgos

| Riesgo | Probabilidad / impacto | Estado y medidas |
| --- | --- | --- |
| Retraso en las entregas de Adriana por su ausencia y otros compromisos | Alta / medio | Abierto. Se le asigna menos carga; Adriana se compromete a entregar sus tareas antes del cierre del sprint (22 de octubre) |

#### 4. Requisitos e issues

- **Requisitos completados:** ninguno (inicio del sprint).
- **Requisitos pendientes o bloqueados:** todos los del Sprint 1, pendientes de empezar.
- **Issues completadas:** ninguna.
- **Issues pendientes o bloqueadas:** las del Sprint 1, ya repartidas en el plan.
- **Bloqueos o dependencias:** las pantallas de viajes dependen de la base de la PWA y del esquema inicial de Supabase (PB-01).

#### 5. Objetivos para la semana siguiente

| Objetivo / tarea | Responsable | Fecha objetivo |
| --- | --- | --- |
| Pipeline CI/CD y servidor Socket.io (PB-02) | Berta | 7 de octubre |
| Proyecto Supabase, esquema inicial y políticas RLS (PB-01.1.2) | Berta | 8 de octubre |
| Iniciar sesión con email y con Google (PB-04 y PB-05) | Daniel | 13 de octubre |
| Esqueleto PWA, rutas y barra inferior (PB-01.1.1) | Adriana | Antes del 22 de octubre |

#### Acuerdos y cierre

- **Acuerdos:** se aprueba la planificación del Sprint 1, con menos carga para Adriana.
- **Próxima reunión:** miércoles, 21 de octubre de 2026, de 19:00 a 20:00.

<a id="acta-2026-10-21"></a>
### Miércoles, 21 de octubre de 2026 — 19:00–20:00

**Asistentes:** Adriana Sainz Sampedro, Berta Castillo Crespo y Daniel Blasco Labarta
**Ausencias y justificación:** ninguna.
**Hito:** Revisión final de S1 — práctica 2 (entrega: 22 de octubre)

#### Orden del día

1. Asuntos de trámite.
2. Revisión de la dedicación semanal.
3. Monitorización de riesgos.
4. Seguimiento de requisitos e issues completadas y pendientes.
5. Marcaje de objetivos para la semana siguiente.

#### 1. Asuntos de trámite

- **Temas tratados:**
  - Revisión final del Sprint 1 antes de la entrega del 22 de octubre.
  - Adriana comunica que se ha retrasado con subir los cambios GitHub: su trabajo del sprint aún no está subido a los repositorios y sus issues siguen abiertas.
  - Preparación del Sprint 2 (del 23 de octubre al 5 de noviembre).
- **Decisiones:**
  - Adriana pondrá GitHub en orden esa misma noche: subirá su código al Backend y al Frontend (le faltan algunos tests) y cerrará sus issues antes de la entrega.
  - Se mantiene el reparto del Sprint 2 previsto en el plan.

#### 2. Dedicación semanal

| Integrante | Dedicación prevista (h) | Dedicación realizada (h) | Desviaciones / comentarios |
| --- | ---: | ---: | --- |
| Adriana Sainz Sampedro | 10 | 12 | Trabajo concentrado al final del sprint, como se acordó el 5 de octubre, sumando la noche del 21 |
| Berta Castillo Crespo | 27 | [completar] | - |
| Daniel Blasco Labarta | 27 | [completar] | - |

#### 3. Riesgos

| Riesgo | Probabilidad / impacto | Estado y medidas |
| --- | --- | --- |
| Retraso en las entregas de Adriana | Alta / medio | Se materializa, pero se mitiga: Adriana sube su trabajo y cierra sus issues la noche del 21 de octubre, dentro del plazo de entrega |
| Las políticas de seguridad (RLS) nuevas no estén aplicadas en Supabase | Media / alto | Abierto. Hay que ejecutar el script de políticas en Supabase tras subir el código |
| Poco margen antes de la entrega del 22 de octubre | Media / alto | Abierto. Adriana asegura que llega a tiempo; se revisará todo la mañana del 22 |
| Carga del Sprint 2 concentrada en pocos días | Media / medio | Abierto. Se hará seguimiento en la reunión del 28 de octubre |

#### 4. Requisitos e issues

- **Requisitos completados en S1:**
  - Berta: pipeline CI/CD y servidor Socket.io (PB-02), diseño del botón de Google (PB-03), crear un viaje (PB-07) y diseño de «Unirse a viaje» (PB-09).
  - Daniel: login con email (PB-04), login con Google (PB-05), registro (PB-06) y cerrar sesión (PB-11).
  - Adriana (subidos la noche del 21): barra inferior (PB-01.1.1), ver mis viajes junto con Berta (PB-08), editar viaje (PB-10), archivar viaje (PB-12) y eliminar viaje (PB-13).
- **Issues completadas:** las de PB-02 a PB-07, PB-09 y PB-11; las de Adriana y las restantes se cierran entre esa noche y la mañana del 22.
- **Bloqueos o dependencias:** ninguno.

#### 5. Objetivos para la semana siguiente (Sprint 2)

| Objetivo / tarea |Fecha objetivo |
| --- | --- | --- |
| Añadir actividad (PB-17) | 27 de octubre |
| Crear una votación (PB-18) | 29 de octubre |
| Registrar un gasto (PB-23) | 3 de noviembre |
| Ver historial de gastos (PB-24) |  4 de noviembre |
| Unirse a un viaje con enlace o QR (PB-15) |  4 de noviembre |
| Votar y ver resultados en tiempo real (PB-19) | 28 de octubre |
| Cerrar una votación (PB-20) | 29 de octubre |
| Fijar destino ganador en el viaje (PB-21) | 2 de noviembre |
| Geolocalizar la dirección de una actividad (PB-26) |  4 de noviembre |
| Ver la agenda del día (PB-16) | 29 de octubre |
| Editar y eliminar actividad (PB-22) |  2 de noviembre |
| Ver balance de cada miembro (PB-25) |  4 de noviembre |

#### Acuerdos y cierre

- **Acuerdos:** Adriana sube su trabajo y cierra sus issues esa noche; el Sprint 1 se entrega el 22 de octubre; el Sprint 2 empieza el 23 de octubre con el reparto del plan.
- **Próxima reunión:** miércoles, 28 de octubre de 2026, de 19:00 a 20:00.

<a id="acta-2026-10-28"></a>
### Miércoles, 28 de octubre de 2026 — 19:00–20:00

**Asistentes:** Adriana D. Sainz Sampedro / Berta Castillo Crespo / Daniel Blasco Labarta  
**Hito:** Seguimiento de S2 — práctica 3 (entrega: 5 de noviembre)

#### Orden del día

1. Asuntos de trámite.
2. Revisión de la dedicación semanal.
3. Monitorización de riesgos.
4. Seguimiento de requisitos e issues completadas y pendientes.
5. Marcaje de objetivos para la semana siguiente.

#### Seguimiento y acuerdos

- **Asuntos de trámite / decisiones:**
- **Dedicación semanal (prevista / realizada por integrante):**
- **Riesgos y medidas:**
- **Requisitos completados / pendientes:**
- **Issues completadas / pendientes / bloqueadas:**
- **Objetivos para la semana siguiente (responsable y fecha):**
- **Acuerdos:**

<a id="acta-2026-11-04"></a>
### Miércoles, 4 de noviembre de 2026 — 19:00–20:00

**Asistentes:** Adriana D. Sainz Sampedro / Berta Castillo Crespo / Daniel Blasco Labarta  
**Hito:** Revisión final de S2 — práctica 3 (entrega: 5 de noviembre)

#### Orden del día

1. Asuntos de trámite.
2. Revisión de la dedicación semanal.
3. Monitorización de riesgos.
4. Seguimiento de requisitos e issues completadas y pendientes.
5. Marcaje de objetivos para la semana siguiente.

#### Seguimiento y acuerdos

- **Asuntos de trámite / decisiones:**
- **Dedicación semanal (prevista / realizada por integrante):**
- **Riesgos y medidas:**
- **Requisitos completados / pendientes:**
- **Issues completadas / pendientes / bloqueadas:**
- **Objetivos para la semana siguiente (responsable y fecha):**
- **Acuerdos:**

<a id="acta-2026-11-11"></a>
### Miércoles, 11 de noviembre de 2026 — 19:00–20:00

**Hito:** Seguimiento de S3 — práctica 4 (entrega: 19 de noviembre)

#### Orden del día

1. Asuntos de trámite.
2. Revisión de la dedicación semanal.
3. Monitorización de riesgos.
4. Seguimiento de requisitos e issues completadas y pendientes.
5. Marcaje de objetivos para la semana siguiente.

#### Seguimiento y acuerdos

- **Asuntos de trámite / decisiones:**
- **Dedicación semanal (prevista / realizada por integrante):**
- **Riesgos y medidas:**
- **Requisitos completados / pendientes:**
- **Issues completadas / pendientes / bloqueadas:**
- **Objetivos para la semana siguiente (responsable y fecha):**
- **Acuerdos:**

<a id="acta-2026-11-18"></a>
### Miércoles, 18 de noviembre de 2026 — 19:00–20:00

**Hito:** Revisión final de S3 — práctica 4 (entrega: 19 de noviembre)

#### Orden del día

1. Asuntos de trámite.
2. Revisión de la dedicación semanal.
3. Monitorización de riesgos.
4. Seguimiento de requisitos e issues completadas y pendientes.
5. Marcaje de objetivos para la semana siguiente.

#### Seguimiento y acuerdos

- **Asuntos de trámite / decisiones:**
- **Dedicación semanal (prevista / realizada por integrante):**
- **Riesgos y medidas:**
- **Requisitos completados / pendientes:**
- **Issues completadas / pendientes / bloqueadas:**
- **Objetivos para la semana siguiente (responsable y fecha):**
- **Acuerdos:**

<a id="acta-2026-11-25"></a>
### Miércoles, 25 de noviembre de 2026 — 19:00–20:00

**Hito:** Seguimiento de S4 — práctica 5 (entrega: 3 de diciembre)

#### Orden del día

1. Asuntos de trámite.
2. Revisión de la dedicación semanal.
3. Monitorización de riesgos.
4. Seguimiento de requisitos e issues completadas y pendientes.
5. Marcaje de objetivos para la semana siguiente.

#### Seguimiento y acuerdos

- **Asuntos de trámite / decisiones:**
- **Dedicación semanal (prevista / realizada por integrante):**
- **Riesgos y medidas:**
- **Requisitos completados / pendientes:**
- **Issues completadas / pendientes / bloqueadas:**
- **Objetivos para la semana siguiente (responsable y fecha):**
- **Acuerdos:**

<a id="acta-2026-12-02"></a>
### Miércoles, 2 de diciembre de 2026 — 19:00–20:00

**Hito:** Revisión final de S4 — práctica 5 (entrega: 3 de diciembre)

#### Orden del día

1. Asuntos de trámite.
2. Revisión de la dedicación semanal.
3. Monitorización de riesgos.
4. Seguimiento de requisitos e issues completadas y pendientes.
5. Marcaje de objetivos para la semana siguiente.

#### Seguimiento y acuerdos

- **Asuntos de trámite / decisiones:**
- **Dedicación semanal (prevista / realizada por integrante):**
- **Riesgos y medidas:**
- **Requisitos completados / pendientes:**
- **Issues completadas / pendientes / bloqueadas:**
- **Objetivos para la semana siguiente (responsable y fecha):**
- **Acuerdos:**

<a id="acta-2026-12-09"></a>
### Miércoles, 9 de diciembre de 2026 — 19:00–20:00

**Asistentes:** Adriana D. Sainz Sampedro / Berta Castillo Crespo / Daniel Blasco Labarta  
**Hito:** Cierre y retrospectiva de S4 — práctica 5

#### Orden del día

1. Asuntos de trámite.
2. Revisión de la dedicación semanal.
3. Monitorización de riesgos.
4. Seguimiento de requisitos e issues completadas y pendientes.
5. Marcaje de objetivos para la semana siguiente y retrospectiva de S4.

#### Seguimiento y acuerdos

- **Asuntos de trámite / decisiones:**
- **Dedicación semanal (prevista / realizada por integrante):**
- **Riesgos abiertos y medidas:**
- **Requisitos completados / pendientes:**
- **Issues completadas / pendientes / bloqueadas:**
- **Retrospectiva de S4 (logros y mejoras):**
- **Objetivos siguientes (responsable y fecha):**
- **Acuerdos:**
