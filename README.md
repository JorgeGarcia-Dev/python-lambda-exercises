![Imagen_Python](images/Banner_Python.png)

# Funciones Lambda

* **A grandes rasgos, las funciones Lambda son funciones anónimas que solo pueden contener una expresión.**

  * Se le llama anónimas porque éstas carecen de un nombre.
  * Éstas no se definen con la palabra reservada **_'def'_**.
  * Éstas funciones pueden tomar cualquier número de argumentos, pero solo pueden contener una expresión.
  * Éstas se definen en una sola línea.
  * Resultan útiles cuando se desea definir una función pequeña de forma concisa.

---

## Sintaxis:

```
lambda argumentos: expresión
```

---

## Ejemplo:

Podemos pasar de esto:

```
"""Función"""

def suma(a, b):
    return a + b

print(suma(5, 5))
```

A esto:

```
"""Función Lambda"""

suma = lambda a, b: a + b
print(suma(5, 5))
```

---

#### En este repositorio puedes encontrar más ejemplos.