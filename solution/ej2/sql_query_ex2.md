# SQL Query 
Como se indicó dentro del archivo README del repositorio, la sentencia fue diseñada para el entorno MySQL, pero debería de poder se utilizada dentro de otros entornos sin perder su funcionalidad, con la excepción de SQL Server de Microsoft.

Como también mencionado, a continuación se indican dos sentencias SQL: la primera solo toma en cuenta las primeras letras del primer nombre de la persona, mientras que la segunda incluye a aquellos que tengan segundos nombres y estos empiecen con las letras especificadas.

**No Toma en Cuenta Segundos Nombres**  
select * from ciudadanos where (nombre like 'Ped%' or nombre like 'San%') and length(apellido) < 15;

**Toma en Cuenta Segundos Nombres**  
select * from ciudadanos where (nombre like 'Ped%' or nombre like 'San%' or nombre like '% San%' or nombre like '% Ped%') and length(apellido) < 15
