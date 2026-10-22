# 4. Definición de hecho

Un elemento del Product Backlog (PBI) se considerará "Hecho" para ser incluido en producción cuando cumpla todas las entradas de la siguiente lista de chequeo:

| Criterio DoD | Detalle de verificación |
| --- | --- |
| **Revisión de código y calidad** | El código fuente debe ser revisado por un miembro distinto al autor. Se elige a la persona que menos tareas tenga en curso en ese punto del proyecto; en caso de que sean iguales, se elige aleatoriamente.<br><br> La revisión consiste en verificar que el código cumple las convenciones del proyecto y que no tiene warnings.<br><br>La revisión se realiza cuando se ha completado el código correspondiente a una PBI.<br><br>Si la revisión no es satisfactoria, se le debe comunicar al autor para que haga las correcciones oportunas. |
| **Pruebas automatizadas (RNF)** | Pruebas unitarias e integración ejecutadas con éxito en el pipeline de CI/CD. |
| **Seguridad y privacidad (RNF)** | Conexiones seguras (HTTPS/WSS). Autenticación con email y contraseña o Google OAuth desde Supabase. Privacidad de datos asegurada mediante políticas RLS en la base de datos. |
| **Usabilidad y accesibilidad (RNF)** | Se ajusta a los distintos tamaños de pantalla de móviles Android. |
| **Documentación** | Documentación actualizada con los nuevos endpoints, siguiendo los estándares de documentación. |
| **Despliegue** | La nueva funcionalidad debe pasar una prueba de humo para asegurar su corrección y ser desplegado correctamente en un dispositivo Android. |
| **Cumplimiento de los criterios de satisfacción** | La entrada de la pila debe cumplir todos los criterios de satisfacción definidos para ella. |
