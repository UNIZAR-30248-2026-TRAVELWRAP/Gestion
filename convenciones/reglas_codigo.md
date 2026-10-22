# Normas de Código

Para las convenciones de nombrado:

* Las clases deben ir en PascalCase (ej. UsuarioController).  
* Las variables y métodos deben ir en camelCase (ej. calcularTotal, idGasto).  
* Las constantes deben ir en mayúsculas separadas por guiones bajos (ej. MAX\_REINTENTOS).  
* Claridad y longitud: Los nombres deben ser autoexplicativos. Queda prohibido usar variables de una sola letra (como x, a, aux) excepto para índices de bucles muy cortos (como i) 

Para la limpieza y validación del código:

* El código debe compilar sin mostrar ningún warning.  
* No debe haber importaciones (imports) que no se estén utilizando.  
* Nada de código comentado: No se debe dejar código comentado por el típico "por si acaso luego hace falta". Para recuperar código antiguo ya usamos Git.  
* Sin rastros de depuración: Prohibido subir console.log, System.out.print o funciones similares de prueba.  
* Variables sin leer: No debe haber variables declaradas a las que luego nunca se les da uso.  
* Formato e Indentación unificada: Todo el equipo debe usar exactamente la misma configuración de indentación (4 espacios, prohibido mezclar espacios y tabuladores). Para que sea automático, se recomienda añadir un archivo .editorconfig al proyecto o configurar el editor para que "formatee al guardar".  
* Manejo de errores: Queda prohibido dejar bloques de excepciones (catch) vacíos. Si se captura un error, al menos debe dejar un registro claro de lo que ha fallado.

