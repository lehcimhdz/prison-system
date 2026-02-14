## CONTEXTO
Estoy construyendo [un proyecto para el sistema penitenciario de la Ciudad de México (puros fines educativos y de simulación)] para [aprender como se estructura, crea, desarrolla y mantiene un pipeline de data engineering totalmente profesional].

## PROBLEMA A RESOLVER

En diversas ocasiones, como servidor público acudí personalmente a varias cárceles de la Ciudad de México, en las que pude observar los siguientes problemas:

1. El ingreso y egreso trata de ser metículoso, pero no siempre se logra. Los servidores públicos, notificadores, funcionarios de derechos humanos, etc. No tienen un sistema centralizado para saber quién está en la cárcel, por qué está ahí, cuánto tiempo lleva, etc. El mecanismo central de identificación personas para todo aquel ser humano será la HUELLA DIGITAL.
2. El ingreso y egreso de visitantes es diferente. Debe existir un registro de quién es, a qué interno visita, qué cosas (artículos personales, de higiene, comida, etc. ingresa).
3. El ingreso y egreso, de limpieza, de mantenimiento, cocineros, custodios, funcionarios, psícologos, médicos, trabajadores sociales, etc. Debe existir un registro de quién es, a qué área va, cuánto tiempo lleva, etc. Datos relevantes, por ejemplo de limpieza su nombre, sueldo, horario. Debe existir un registro de quién es, a qué área va, cuánto tiempo lleva, etc. Datos relevantes, por ejemplo de limpieza su nombre, sueldo, horario.
4. El ingreso y egreso de proveedores de alimentos, de servicios, de mantenimiento, etc. Debe existir un registro de quién es, a qué área va, cuánto tiempo lleva, etc. El registro debe ser prevío, vínculado a un contrato o licitación, etc.
5. El ingreso y egreso de vehículos, de transporte, de servicios, de mantenimiento, etc. El registro debe ser prevío, vínculado a un contrato o licitación, etc.
6. El ingreso y egreso de material, insumos, armamento, equipo táctico, etc. Debe ser prevío, vínculado a un contrato o licitación, etc.
7. Los principales: los presos. En el momento en el que ingresan deben existir datos judiciales, de salud, datos personales, etc. Las fotos, perfiles, carácteristicas físicas, huellas digitales, se deben almacenar. Durante su estancia deberá existir un registro de su comportamiento, de su salud, de su estado psicológico, de sus visitas, de sus comunicaciones, de sus actividades, de su trabajo, de su educación, de su rehabilitación, de su reinserción social, sanciones, etc.
8. El dinero en efectivo es una fuente de corrupción, por lo que se debe evitar su ingreso y permanencia en el centro penitenciario. Se debe implementar un sistema de monedero electrónico para los internos. Este monedero electrónico debe estar vinculado a una cuenta bancaria del interno, la cual debe ser alimentada por depósitos en efectivo o transferencias bancarias. Los internos podrán usar este monedero electrónico para comprar productos en la tienda del centro penitenciario, para pagar servicios, para realizar llamadas telefónicas, etc. El dinero que reciban de su trabajo dentro del centro penitenciario, se almacenará en ese monedero electrónico.
9. Deberá existir un registro metículoso de todas las compras, ventas, depósitos, retiros, transferencias, etc. que se realicen con el monedero electrónico de cada interno. 
10. Al momento de abandonar el centro penitenciario por absolución, cumplimiento de la sentencia, traslado a otro centro penitenciario, etc. Se deberá realizar un registro de su egreso, el cual deberá incluir el saldo que tenga en su monedero electrónico, el cual deberá ser entregado en efectivo o transferido a una cuenta bancaria del interno. 
11. Los custodios deben apegarse a un sistema de disciplina extrema y evitar actos de corrupción, de tortura, de extorsión, etc. Existirá un registro de su desempeño, de sus sanciones, de sus amonestaciones, etc.
12. El centro penitenciario se organiza por bloques: perimetro exterior, perimetro interior, dormitorios, áreas comunes, gobierno, administrativo, etc. Deben existir registros específicos de cualquier persona que sale/entra de alguna área específica, horario, etc.
13. El centro penitenciario es una unidad con todos esos datos, pueden existir más centros penitenciarios con los mismos datos.


## OBJETIVO ESPECÍFICO
Necesito implementar [un sistema de data engineering para el centro penitenciario de la Ciudad de México] que haga [que toda la información del centro penitenciario sea centralizada, accesible, segura, escalable, y que permita tomar decisiones informadas].

## CONSTRAINTS
- Tech stack: [PYTHON, POSTGRESQL, AIRFLOW, DASK, KUBERNETES, DOCKER, MINIO, KAFKA, spark, etc.]
- Performance: [REQUISITOS SI APLICA]
- Debe ser [PRODUCTION-READY]

## REQUEST
1. ¿Cómo se estructuran las carpetas en un proyecto data engineering?
2. ¿Cómo se implementa un pipeline de data engineering profesional?
3. ¿Cómo se implementa un sistema de data engineering profesional?
4. ¿Qué hace y cuál es la función de cada tecnología?
5. ¿Qué hace y cuál es la función de cada bloque de código?

NO me des solución completa, dame una GUIA Y ENSÉÑAME PASO A PASO COMO SI FUERA YO EL DESARROLLADOR JUNIOR. 

Debes agregar markdowns, bullets, negritas, etc. Para que sea fácil de leer y entender. Debes agregar markdowns explicando cada paso, cada tecnología, cada bloque de código, etc. Estos los incluirás en .gitignore.

Usa fake data.

Ejecutemos.