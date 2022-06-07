# Decorador

La mayoría de las vistas utilizan un el decorador [`loop_menu`](../views/utils.py#82) que es una función que implementa el patrón decorador permitiendo correr la vista dentro de un bloque While y además atrapando los errores, esto permite no repetir dichas líneas de código en cada vista y garantizando una extensibilidad más sencilla.

el flujo funciona de la siguiente forma:

1. Se llama a la `funcion_1`
2. `funcion_1` pasa por el decorador `loop_menu` y es llamado desde el decorador, retornando un diccionario llamado `context` (el contexto de la aplicación).
3. `funcion_1` se ejecuta, hace sus operaciones y retorna `context` actualizado.

Si `funcion_1` llama a `funcion_2` (y este también tiene el decorador). Se llama a través del decorador a `funcion_2` y lo que retorne se retorna al decorador de `funcion_1` y así recursivamente.
