# Ejercicio 6 - README

## Solución
La solución del ejercicio se encuentra dentro del archivo `knn.py`, que hace uso del archivo `teleCust1000t.csv`.

Dentro de este archivo, se ha diseñado el algoritmo de [k-nearest-neighbor](https://es.wikipedia.org/wiki/K_vecinos_m%C3%A1s_pr%C3%B3ximos), el cual se utiliza para, acompañado por el data set provisto, predecir el dato 'custcat' de los clientes.

Para lograr esto se utilizaron tres funciones principales:
- `distance`: Esta función, dado el tipo y dos registros, retorna la distancia especificada entre los dos registros. Se puede elegir entre la distancia [Euclidiana](https://es.wikipedia.org/wiki/Distancia_euclidiana) o la distancia [Manhattan](https://es.wikipedia.org/wiki/Geometr%C3%ADa_del_taxista).
- `getNeighbors`: Dados un data set de entrenamiento, un registro, y la cantidad de vecinos deseados (configurable), retorna una lista con la cantidad de vecinos especificada que esten mas cerca del registro dado.
- `predictCustcat`: Dados un data set de entramiento, un registro, y la cantidad de vecinos deseados (configurable), retorna la predicción del valor 'custcat' para el registro dado, basandose en el valor 'custcat' más "famoso" dentro de sus vecinos más cercanos.

A través de estas funciones y de la lectura del data set dentro del archivo CSV provisto, el módulo predice el valor 'custcat' del registro dado y lo retorna. A su vez, el usuario, haciendo uso de la función `persist_prediction` puede persistir las predicciones dentro del archivo `teleCust1000t.csv` para ser referenciadas en futuras predicciones. 

Además, se presenta el diccionario `services` para traducir el dato predecido al nombre del servicio real. También se encuentra la función `formatCSV` que, dado una lista con los datos del un archivo CSV con las misma firma que el archivo `teleCust1000t.csv` devuelve la misma list pero con sus variables traducidas a números enteros (int).

## Modo de Prueba

### Archivo `test.py`
Para esto se necesitará de:
- [Python](https://www.python.org/downloads/)
- Los archivos `knn.py`, `test.py` y `teleCust1000t.csv` encontrados en este directorio

Una vez descargados, colocar los tres archivos de este directorio dentro de una misma carpeta y abrir una ventana de terminal dentro de la carpeta. Para testear el módulo, correr el siguiente comando:
```
python test.py
```

Una vez se ejecute el comando, se mostrará en pantalla un breve saludo y se pedirá al usuario ingresar el tipo de input: *Manual* o *Por archivo CSV*.

Cualquiera sea elegido, se le pedirá a continuación ingresar la cantidad de vecinos a tomar en cuenta y el tipo de distancia a utilizar. Con estos datos seleccionados, el funcionamiento se divide en dos dependiendo del tipo de input elegido:

#### Manual
Si se escogió el modo manual, se pedirá a continuación ingresar los valores de cada campo, con su tipo indicado al lado. Una vez ingresados se imprime en pantalla la predicción obtenida.

Aquí se da la opción de persistir el dato obtenido si así se desea, y de predecir el dato de otro cliente, en cual caso se vuelven a pedir los datos y se empieza de nuevo.

#### Por archivo CSV
Si se escogiónel modo por archivo CSV, se debe colocar dentro del mismo directorio un archivo CSV `input.csv` con la misma firma que el archivo `teleCust1000t.csv` menos el dato 'custcat'. 

Cuando se ejecute el comando, el programa leerá este archivo y generará otro archivo CSV `output.csv` con los valores de 'custcat' predecidos agregados al registro de cada cliente.

Además, se imprimirán en consola los valores obtenidos y se dará la opción de persistirlos en el archivo `teleCust1000t.csv` para ser usados en futuras predicciones.

**Nota:** En el directorio `ibm/resources` se dispone de un archivo `input.csv` para probar este modo, y de un archivo `output.csv` para comprobar los valores predecidos. El segundo archivo fue generado con el número de vecinos de 10 y el tipo de distancia 0.

### Usando `knn.py` como libería
Utilizando la sentencia `import knn` dentro de un archivo de Python que se encuentre dentro del mismo directorio, se puede hacer uso de las funciones del mismo.
