# Solución de Prueba Técnica - IBM - 2022 
En este repositorio se encontrará la solución a la prueba técnica de IBM Blue Journey de 2022, realizada por **Gonzalo Ferreira**.

## Introducción
El repositorio está estructurado por dos directorios: *solution* y *resources*.

### Solution
Este directorio contiene las soluciones a los diferentes ejercicios propuestos que han sido realizados.

La carpeta contiene subdirectorios titulados '*ejX*', donde 'X' es el número de ejercicio al que corresponde la solución contenida en él.  
Además, cada subdirectorio contiene un archivo README que explica brevemente el razonamiento, desarrollo, aplicación, y prueba de cada ejercicio, así como información adicional pertinente.

### Resources
Este diretorio contiene archivos adicionales útiles a la hora de poner en prueba las soluciones, o relevantes a ellas.

En el directorio de *solution*, se hace referencia a los archivos aquí encontrados, y se explica su uso o relevancia.  
El directorio cuenta también con un propio archivo README que explica el origen de cada archivo.

## Solución
A continuación, por cada ejercicio realizado se da una breve descripción de su solución, se lista el directorio de los archivos, y se notan datos relevantes.

### Ejercicio 2
Solución encontrada en: *solution/ej2*.

Dentro de la carpeta se encuentra el archivo de texto *sql_query.txt*, el cuál contiene la consulta SQL pedida por el ejercicio.  
En el directorio de *resources*, se encuentra un data set titulado *sqlDataSet.csv* que puede ser utilizado para probar el correcto funcionamiento de la consulta.

**Tomar en Cuenta**  
- La consulta fue hecha bajo la gestión de base de datos de MySQL, pero su estructura es génerica y puede ser utilizada bajo otros sistemas. SQL Server de Microsoft es una excepción ya que define una de las funciones utilizadas bajo otro nombre (LEN vs. LENGTH).
- Se incluye y se explica dentro del archivo provisto, que existen dos consultas SQL: una toma en cuenta que el campo *nombre*, pude tener dos nombres, e incluye a aquellos cuyo segundo nombre también comience con las letras especificadas. La otra consulta ignora este detalle.
