# Normas de la API

Para la documentación de los endpoints (en OpenAPI 3.0):

* Ruta: Debe indicar la URL exacta (ej. /api/gastos/{id}).  
* Tipo: Debe indicar el método HTTP correspondiente (GET, POST, PUT, DELETE).  
* Entrada (Request): Debe especificar qué datos o JSON necesita recibir.  
* Salida (Response): Debe especificar qué devuelve y los posibles códigos de estado (ej. 200 OK con el JSON del gasto, o 400 si faltan parámetros).

Para el diseño de las rutas y formato:

* Las URL deben usar sustantivos en plural, nunca verbos (ej. usar /usuarios en lugar de /getUsuarios).  
* La entrada y salida de datos siempre debe realizarse en formato JSON.  
* Los mensajes de error deben seguir siempre una misma estructura (ej. devolver siempre {"error": "mensaje descriptivo"}).

