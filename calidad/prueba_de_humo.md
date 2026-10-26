# Prueba de humo

Comprobación manual y rápida (unos 5 minutos) de que la aplicación arranca y la funcionalidad nueva funciona en un **móvil Android real** (Android 12 o superior), con el backend y la base de datos reales. No sustituye a las pruebas automáticas: sirve para detectar lo que estas no ven (configuración, despliegue, datos reales, tamaño real de pantalla).

## Preparación

1. Aplicar en Supabase los scripts SQL que haya cambiado la PBI (ver [normas de base de datos](../convenciones/reglas_base_de_datos.md)).
2. Abrir la aplicación en el móvil: la versión desplegada o, mientras no haya despliegue, el servidor de desarrollo accesible desde la red local.
3. Usar una cuenta de prueba, nunca datos personales reales de terceros.

## Pasos

1. **Arranque:** la aplicación carga sin pantalla en blanco y se puede iniciar sesión.
2. **Navegación básica:** se llega a «Mis viajes» y se abre un viaje.
3. **Funcionalidad de la PBI:** se recorre su flujo principal de principio a fin con datos reales y se comprueba que el resultado se guarda (al recargar sigue ahí).
4. **Un caso de error:** se provoca al menos uno (por ejemplo, un dato no válido o una acción sin permiso) y la aplicación muestra un mensaje comprensible.
5. **Varios usuarios** (si la PBI es colaborativa): un segundo usuario del viaje ve el cambio.
6. **Pantalla:** en vertical, sin scroll horizontal ni elementos cortados o tapados por el teclado.

Si falla algún paso, la PBI no está hecha: se corrige y se repite la prueba.
