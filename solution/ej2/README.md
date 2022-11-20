# Ejercicio 2 - README

## Tener en Cuenta
Las consultas SQL formuladas para resolver el ejercicio fueron diseñadas para la gestión de base de datos de MySQL. Si bien su estructura es suficientemente génerica para que pueda ser utilizada bajo cualquier lenguaje de SQL, puede ocurrir, como sucede para SQL Server de Microsoft, que esta no funcione correctamente debido a la definición de la función LENGTH (llamada LEN en SQL Server y otros).

## Consultas SQL
Para la resolución del ejercicio se ha tenido en cuenta la posibilidad de que la columna `nombre` en la tabla `ciudadanos` pueda contener dos nombres. Para ello se han desarrollado dos consultas SQL: una que incluye a aquellos cuyo segundo nombre comienze con las letras especificadas ('Ped' o 'San') y otra que no.

A continuación se muestran las consultas:

### NO Incluye Segundos Nombres
```
SELECT * FROM ciudadanos WHERE (nombre LIKE 'Ped%' OR nombre LIKE 'San%') and LENGTH(apellido) < 15
```

### SI Incluye Segundos Nombres
```
SELECT * FROM ciudadanos WHERE (nombre LIKE 'Ped%' OR nombre LIKE 'San%' OR nombre LIKE '% San%' OR nombre LIKE '% San%') and LENGTH(apellido) < 15
```

## Modo de Prueba
Para probar el correcto funcionamiento de la consulta, se dispone de dos formas:

### Prueba Online
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
Para la prueba local se puede utilizar cualquier gestor de base de datos, aunque se recomienda se use [MySQL](https://www.mysql.com/downloads/) por razones previamente especificadas.  
Sea cual sea el gestor, crear una tabla `ciudadanos` con con las columnas `nombre` y `apellido`.  

Esta tabla se puede cargar con los datos encontrados en el archivo `listaPersonas100.csv` o el archivo `listaPersonas.csv` encontrados en el directorio `ibm/resources`. El primer archivo contiene únicamente 100 registros levemente editados, mientras que el segundo contiene mas de 100.000 registros que no han sido modificados. Tener en cuenta que ambos archivos contienen mas columnas que el nombre y el apellido, las cuales pueden ser despreciadas o incluidas en la tabla.  
En su defecto, la tabla puede ser cargada con datos provenientes de otras fuentes, siempre y cuando se mantengan las columnas `nombre`y `apellido`.

Con la tabla `ciudadanos` cargada, simplemente efectuar cualquier de las dos consultas SQL para verificar su funcionamiento.
