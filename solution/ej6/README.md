# Ejercicio 6 - README

## Solución
La solución del ejercicio se encuentra dentro del archivo `knn.py`, que hace uso del archivo `teleCust1000t.csv`.

Dentro de este archivo, se ha diseñado el algoritmo de [k-nearest-neighbor](https://es.wikipedia.org/wiki/K_vecinos_m%C3%A1s_pr%C3%B3ximos), el cual se utiliza para, acompañado por el data set provisto, predecir el dato 'custcat' de los usuarios ingresados.

Para lograr esto se utilizaron tres funciones principales:
- `distance`: Esta función, dado el tipo y dos registros, retorna la distancia especificada entre los dos registros. Se puede elegir entre la distancia [Euclidiana](https://es.wikipedia.org/wiki/Distancia_euclidiana) o la distancia [Manhattan](https://es.wikipedia.org/wiki/Geometr%C3%ADa_del_taxista).
- `getNeighbors`: Dados un data set de entrenamiento, un registro, y la cantidad de vecinos deseados (configurable), retorna una lista con la cantidad de vecinos especificada que esten mas cerca del registro dado.
- `predictCustcat`: Dados un data set de entramiento, un registro, y la cantidad de vecinos deseados (configurable), retorna la predicción del valor 'custcat' para el registro dado, basandose en el valor 'custcat' más "famoso" dentro de sus vecinos más cercanos.

A través de estas funciones y de la lectura del data set dentro del archivo CSV provisto, el módulo predice el valor 'custcat' del registro ingresado y lo muestra en pantalla. A su vez, si el usuario válida el valor predecido, este se registra dentro del archivo `teleCust1000t.csv` para su uso en futuras predicciones. 

## Modo de Prueba
Para probar el correcto funcionamiento de la solución se necesitará de:
- [Python](https://www.python.org/downloads/)
- Los archivos `knn.py` y `teleCust1000t.csv` encontrados en este directorio

Una vez descargados, colocar los dos archivos de este directorio dentro de una misma carpeta y abrir una ventana de terminal dentro de la carpeta. Para ejecutar el módulo, correr el siguiente comando:
```
python knn.py
```

### Configuración
Para configurar el módulo, abrir el archivo `knn.py` con cualquier editor de texto.

Una vez dentro, buscar la sección de `# CONFIGURACION`. Dentro de esta hay tres variables a modificar:
- `NUM_NEIGHBORS`: Esta variable define la cantidad de vecinos a considerar a la hora de buscar los K vecinos más cercanos. Debe ser mayor a 0.
- `DISTANCE_TYPE`: Esta variable determina el tipo de distancia a usar. 0 indica la distancia euclidiana, y 1 indica la distancia Manhattan.
- `INPUT_METHOD`: Esta variable indica si se proveerán los registros a predecir uno por uno a mano a través de la consola, o si se proporcionará un archivo CSV con los registros. 0 indica uno a uno, y 1 indica por CSV. Esto se define mejor en las siguientes dos secciones.

### 1 a 1
Si se selecciona el `INPUT_METHOD = 0`, una vez se ejecute el módulo, se pedirá al usuario ingresar los datos del cliente cuyo valor de 'custcat' se desea predecir. Estos datos son los mismos que fueron proporcionados por el data set de entrenamiento. 

Una vez ingresados, el módulo muestra en pantalla el valor predecido. Luego, el usuario puede elegir si válidar la predicción o no. Si la válida, esta se registra dentro del data set de entrenamiento para teneral en cuenta en futuras predicciones.

Cualquiera sea la respuesta, el sistema pregunta al usuario si se desea predecir el valor 'custcat' de otro cliente. Si asi lo es, se repite la operación de ingreso de datos, validación de la predicción, y nuevamente se pregunta si se quiere continuar prediciendo. En caso contrario, el módulo termina.

### Archivo CSV
Si se selecciona el `INPUT_METHOD = 1`, se debe colocar en la misma carpeta que los archivos `knn.py` y `teleCust1000t.csv`, un archivo llamada `input.csv`. Este debe contener los registros que se desean probar estructurados de la misma manera que aquellos provistos en el data set de entrenamiento, con la diferencia de que el valor 'custcat' este nulo.

Una vez de ejecute el módulo, este leera los registros dentro del archivo `input.csv` y predicirá sus valores 'custcat'. Una vez logrado, se generará en la misma carpeta un archivo `output.csv` con los registros más el valor estimado. 

Luego, se mostrarán en pantalla los valores predecidos y se le preguntará al usuario si desea validarlos. De ser así, estos son guardados en el data set de entrenamiento para su futuro uso en predicciones.

Para este caso, se encuentran en el directorio de `ibm/resources`, dos archivos para poner en prueba este uso. El primero es `input.csv`, el cual debe ser colocado en la misma carpeta que los otros archivos como indicado previamente. El otro es `output.csv`; los resultados del mismo fueron obtenidos usando `NUM_NEIGHBORS = 15` y `DISTANCE_TYPE = 0`.
