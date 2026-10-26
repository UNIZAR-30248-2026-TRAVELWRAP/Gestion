# Diseño y visualización móvil

* Resoluciones soportadas: La interfaz debe adaptarse correctamente a pantallas de teléfonos móviles, desde un mínimo de 320px de ancho (móviles pequeños/antiguos) hasta pantallas grandes de unos 430px de ancho (tipo "Pro Max" o equivalentes). No se garantiza ni se diseña para su uso en tablets o navegadores de escritorio.  
* Orientación de pantalla: La aplicación estará diseñada para usarse estrictamente en orientación vertical (Portrait). La interfaz no girará si el usuario pone el móvil en horizontal.  
* Eliminación del *scroll* horizontal: Queda prohibido que la pantalla tenga desplazamiento lateral; todo el contenido debe caber a lo ancho de la pantalla del móvil.
* Textos largos: Los nombres, destinos y demás textos que escribe el usuario no deben romper la maquetación. Se cortan con puntos suspensivos o pasan a la línea siguiente.
* Diseño de referencia: Las pantallas siguen el prototipo de Figma del proyecto y los tokens de estilo (`styles/tokens.ts`).

# Estados de la interfaz

* Errores: Cuando una acción falla (sin conexión, sin permiso, datos no válidos...), se muestra un mensaje comprensible para el usuario, nunca un código técnico ni una pantalla en blanco.
* Acciones en curso: Mientras se envía una acción, su botón se desactiva o indica que está trabajando, para que no se pueda enviar dos veces.
* Listas vacías: Si una lista no tiene elementos, se muestra un texto que lo explique y, si procede, cómo añadir el primero.
* Acciones irreversibles: Borrar, archivar o cerrar algo pide confirmación antes de hacerlo.

# Accesibilidad e Interacción táctil

* Contraste de colores: Los textos e iconos deben tener un contraste lo suficientemente alto respecto al fondo para que la aplicación pueda leerse bien incluso en exteriores o con luz solar directa.  
* Adaptación del teclado virtual: Al pulsar sobre un campo de texto, el teclado del móvil debe adaptarse al tipo de dato (por ejemplo, mostrar el teclado numérico si es un campo para introducir un precio, o el teclado con el símbolo "@" si es un login por email).
* Nombres accesibles: Todo botón, enlace y campo tiene un nombre accesible: su texto visible, una etiqueta (`label`) o, si solo tiene un icono, un `aria-label` (ej. «Volver»). Es lo que leen los lectores de pantalla y lo que usan las pruebas para encontrar los elementos.
* Elementos táctiles: Los botones e iconos pulsables tienen un tamaño suficiente para pulsarlos con el dedo (al menos unos 36px) y no están tan juntos que se pulse otro por error.
* Información no solo por color: El estado de algo (seleccionado, error, completado) no se indica solo con un color: se acompaña de un texto o un icono.
