# Ejercicio 7 Java VER - README

## Tomar en Cuenta
La solución fue desarrollado en [Spring Boot](https://spring.io/projects/spring-boot) utilizando Spring Tools 4 con Maven como manager. Está fue exportada como JAR (`api-rest.jar`) para simplificar el testeo, pero también se provee el código fuente dentro del proyecto de Spring Boot (directorio `api`).  

## Solución
La solución implementa una API REST con un método GET con la firma `/api/predict/custcat`, tomando como parámetro un JSON con los datos del cliente cuyo valor de 'custcat' se desea obtener.

Estos datos son válidados, asegurandosé de que todo dato exista, y que el campo "marital" tenga como valor únicamente "married" o "single". En caso de que esta validación falle, se devuelve un error HTTP 400 con un mensaje adecuado.

Si se logra la validación, se busca el archivo CSV `teleCust1000t.csv` dentro del directorio `C:\`. Una vez encontrado, se busca el registro indicado en JSON. Si es encontrado, se devulve el valor 'custcat' más un estado HTTP 200. Si no lo es, se devuelve un error HTTP 500 con un mensaje adecuado.

## Modo de Prueba
Para testear la solución se necesita tener [Java](https://www.java.com/en/) instalado, de los archivos `api-rest.jar` y `teleCust1000t.csv` encontrados en el directorio, y del programa [Postman](https://www.postman.com/) para enviar solicitudes a la API.

Con todo descargado, seguir los siguientes pasos:
1. Colocar en `C:\` el archivo `teleCust1000t.csv`
2. Ejecutar el archivo `api-rest.jar`
2. Abrir Postman
3. Seleccionar como método `GET`
4. Como dirección colocar `http://localhost:8080/api/predict/custcat`
5. En la sección de Body, seleccionar RAW, tipo JSON, y colocar el registro cuyo valor 'custcat' se desea conocer en formato JSON
6. Enviar la solicitud
7. Se debería de recibir el valor de 'custcat' deseado, o de lo contrario un comentario con cual fue el error
