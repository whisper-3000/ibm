# Ejercicio 7 Python VER - README

## Requerimientos
La solución a este ejercicio fue diseñada utilizando la libería de [Flask](https://flask.palletsprojects.com/en/2.2.x/), que provee un framework para el desarrollo de aplicaciones web. También se hace uso de la librería de [Schema](https://pypi.org/project/schema/) para la validación de datos.

Ambas de estas librerías pueden ser instaladas con [Pip](https://pypi.org/project/pip/), ejecutando los siguientes comandos:
```
pip install Flask
pip install schema
```

## Solución
La solución implementa un método GET con la firma `/api/predict/custcat`, que toma en el body un JSON con los datos que se desean predecir. De estos se verifica que sean del tipo requerido, que todos existan, y que el campo "marital" tenga como valor "married" o "single". En caso contrario se retorna un error HTTP 400 con un comentario adecuado.

Además, se puede enviar dos parámetros: `num_neighbors` y `distance_type`. El primero especifica la cantidad de vecinos a tomar en cuentra, mientras que el otro especifica el tipo de distancia a utilizar. Ambos son opcionales, y si alguno no es provisto se usa como defecto los valores de '10' y '0' respectivamente.

## Modo de Prueba
Para probar el correcto uso de la solución se necesitará de 3 archivos:
- `api.py`: El archivo con la solución en si.
- `knn.py`: Archivo del ejercicio 6 que contiene el predictor.
- `teleCust1000t.csv`: Data set de entrenamiento para el predictor.

Además se requiere de tener instaladas las dos librerías mencionadas en la sección de Requerimientos.

Para el testeo del método GET se recomienda usar la aplicación [Postman](https://www.postman.com/), que permite fácilmente enviar solicitudes HTTP.

Una vez descargado todo, colocar los tres archivos de este directorio en una misma carpeta y abrir una terminal en ella. Luego, seguir los siguientes pasos para probar su uso:
1. Abrir el servidor de Flask con el siguiente comando: `flask --app api run`
2. Abrir Postman
3. Seleccionar el método GET y como dirección colocar: `http://127.0.0.1:5000/api/predict/custcat`
4. En la opción de Body seleccionar RAW y tipo JSON
5. Escribir en el recuadro la figura JSON con los datos del cliente cuyo valor se desea predecir
6. (Opcional) En la opción de Parámetros agregar 'num_neighbors' y/o 'distance_type' y asignarles valores aceptables
7. Enviar la solicitud, se debería devolver el status HTTP 200 y el valor predecido
