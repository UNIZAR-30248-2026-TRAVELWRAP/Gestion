# Revisión de código y calidad

Toda PBI pasa por una revisión de código antes de cerrarse. El objetivo es encontrar errores antes de que lleguen a la demo y que el código del equipo sea homogéneo. No es un examen a la persona autora.

## Quién revisa

- Siempre una persona distinta a la autora.
- Revisa la persona con menos tareas en curso en ese momento. Si hay empate, se elige al azar.
- Si la PBI toca frontend y backend, revisa ambas partes la misma persona, para que vea el flujo completo.

## Cuándo y cómo

1. Cuando el código de la PBI está terminado y su CI está en verde, la persona autora pide la revisión.
2. Quien revisa lo hace en un plazo de **2 días laborables** y deja sus comentarios al autor.
3. Cada comentario puede ser:
   - **Bloqueante:** hay que corregirlo antes de cerrar la PBI (un error, una regla incumplida, falta una prueba...).
   - **Sugerencia:** mejora opcional. La persona autora decide si la aplica.
4. La persona autora corrige los bloqueantes en commits nuevos y avisa. Quien revisa comprueba solo esos cambios.
5. Cuando el revisor acepta los cambios este punto ya queda cumplido.

## Lista de comprobación

### Funcionalidad
- [ ] Hace lo que dicen los criterios de satisfacción de la PBI, también en los casos de error: sin conexión, datos no válidos, sin permiso, recurso inexistente...
- [ ] Se ha probado la funcionalidad en ejecución, no solo leyendo el código.

### Convenciones y limpieza
- [ ] Cumple las [normas de código](../convenciones/reglas_codigo.md): nombres, sin código comentado, sin trazas de depuración, sin imports ni variables sin usar.
- [ ] Sigue la estructura de carpetas y el estilo del código que ya existe (pantallas en `screens`, llamadas a la API en `services`, controlador → servicio en el backend...).
- [ ] No duplica lógica que ya existe en el proyecto; si la necesita en dos sitios, la extrae.
- [ ] Los nombres, comentarios y textos de la interfaz están en español y sin faltas.

### Pruebas
- [ ] Hay pruebas nuevas en los niveles que indica la [estrategia de pruebas](estrategia_de_pruebas.md) y comprueban el comportamiento, no detalles internos.
- [ ] Las pruebas fallarían si la funcionalidad se rompiera (no pasan siempre).

### Seguridad y datos
- [ ] Cumple las [normas de seguridad](../convenciones/reglas_seguridad.md): sesión obligatoria, validación en el backend, RLS en las tablas nuevas, sin secretos.
- [ ] Los cambios de base de datos siguen las [normas de base de datos](../convenciones/reglas_base_de_datos.md) y los scripts se pueden ejecutar varias veces.

### API y documentación
- [ ] Los endpoints siguen las [normas de la API](../convenciones/reglas_API.md) y están en OpenAPI y Postman.
- [ ] La documentación generada está al día (`npm run docs:check` en el backend).

### Interfaz
- [ ] Se ve bien a 320 y a 430 px de ancho y cumple las [normas de diseño móvil](../convenciones/reglas_responsive_movil.md).
- [ ] Muestra los errores al usuario con mensajes comprensibles y no se queda en blanco mientras carga o si falla.

## Calidad estática

Quien revisa comprueba también que:

- **Frontend:** `npm run build` (que incluye `tsc -b`) y `npm run lint` terminan sin errores ni warnings.
- **Backend:** `npm test` y `npm run docs:check` pasan.
- **SonarCloud:** el Quality Gate del análisis de la CI está en verde, sin bugs, vulnerabilidades ni *security hotspots* nuevos sin revisar. Si Sonar marca un falso positivo, se justifica en la revisión en lugar de ignorarlo sin más.

