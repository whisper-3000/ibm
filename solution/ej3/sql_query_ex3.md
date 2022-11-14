# SQL Query Ex3
A continuación se presenta la consulta SQL que retorna los nombres únicos ordenados alfabeticamente:

select nombre from ciudadanos group by nombre having count(*) = 1 order by nombre
