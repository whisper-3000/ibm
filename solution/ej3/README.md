# Ejercicio 3 - README

## Tener en Cuenta
Al igual que en el ejercicio 2, las consultas SQL proporcionadas fueron modeladas bajo el gestor de base de datos MySQL. En este ejercicio en particular, una de las consultas hace uso de una función propia de MySQL, la cual puede no existir en otros gestores, o tener un diferente nombre.

## Consultas SQL
Nuevamente como en el ejercicio anterior, se ha tenido en cuenta la posibilidad de que en la columa `nombre`, exista más de un solo nombre. Para esto se han desarrollado dos consultas SQL:
- La primera toma en consideración a ambos nombres, y considera el nombre 'único' si la combinación de ambos nombres es única. Es decir, bajo esta consulta, los nombres `Gerardo Tomas`, `Gerardo Nicolas` y `Juan Gerardo` son todos 'únicos'.
- La segunda consulta toma en consideración únicamente los primeros nombres, y los toma como 'únicos' si no se repiten. Es decir que `Gerardo Tomas` pasaría a ser solamente `Gerardo`, al igual que `Gerardo Nicolas`, y por lo tanto ninguno de los dos sería 'único'. Sin embargo, asumiendo que no hay nadie llamado `Juan`, el nombre `Juan Gerardo` si se consideraría 'único' ya que no se toma en cuenta el segundo nombre.

### SI Toma en Cuenta Segundos Nombres
```
SELECT nombre AS nombres_unicos FROM ciudadanos GROUP BY nombres_unicos HAVING COUNT(*) = 1 ORDER BY nombres_unicos 
```

### NO Toma en Cuenta Segundos Nombres
```
SELECT SUBSTRING(nombre,' ',1) AS nombres_unicos FROM ciudadanos GROUP BY nombres_unicos HAVING COUNT(*) = 1 ORDER BY nombres_unicos 
```

## Modos de Prueba
Para probar el correcto funcionamiento de las consultas existen dos formas:

### Prueba Online (Reducida)
Para esta prueba se requerirá de dos cosas:
- Archivo `listaPersonas100.csv` encontrado en el directorio `ibm/resources`
- Página web [SQL Fiddle](http://www.sqlfiddle.com/)

Una vez en la página web y con el archivo descargado, seguir las siguientes instrucciones:
1. Hacer click en el botón `Text to DDL` en la parte superior de la página
2. En el campo `Table Name` escribir `ciudadanos`
3. En el campo inferior, copiar y pegar el contenido del archivo `listaPersonas100.csv` en su totalidad
4. Hacer click en el botón `Append to DLL`
5. Hacer click en el botón `Build Schema`
6. Copiar y pegar en el segundo recuadro la consulta SQL deseada
7. Hacer click en el botón `Run SQL`
8. En la parte inferior de la página se podrá apreciar el resultado de las consultas

### Prueba Local
Para la prueba local se requiere del gestor de base de datos [MySQL](https://www.mysql.com/downloads/).

Una vez descargado, crear una tabla de nombre `ciudadanos` con las columnas `nombre` y `apellido`.  
Cargar dicha tabla con los archivos `listaPersonas100.csv` o `listaPersonas.csv` encontrados en `ibm/resources`, o con datos provenientes de otra fuente.

Con la tabla cargada, ejecutar las consultas SQL y comprobar los resultados.
