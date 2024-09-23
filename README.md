# Prácticas para la codificación segura

Este es un repositorio un ejercicio práctico para la charla de "Prácticas para la codificación segura".

## Ejercicio

En el repositorio existen test unitarios que están testeando dos entradas, el primer test `test_sql.py` para prevenir inyecciones SQL y el segundo test `test_number_input.py` para validar que la entrada sea de tipo numérico exclusivo.

Ambas entradas están en el archivo `inputs.py`, pero las validaciones se deben hacer utilizando los decoradores ya creados en el archivo `validators.py`.

- La función `pattern_validator` es la encargada de validar las inyecciones SQL
- La función `number_checker` es la encargada de validar que el valor sea exclusivamente numérico.

En ambos casos, si el input es invalido, se debe retornar un `raise ValueError('')`

Para poder ejecutar los test, se ha de ejecutar en la terminal el comando `python -m unittest`

El objetivo es que todos los test ya creados y probando distintos input funcionen al 100%

```
python -m unittest
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```