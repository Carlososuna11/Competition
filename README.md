# UCAB Competición

Una empresa que organiza competiciones le ha contratado a usted para que le desarrolle una
aplicación que le permita analizar los resultados de su última competencia. Ha requerimiento suyo
los datos de la competencia le serán suministrado en un archivo txt, el cual contendrá en cada línea
los datos separados por coma de cada participante.
Para dar cumplimiento al requerimiento, usted va a desarrollar una aplicación que implementará la
siguiente funcionalidad:

- La lógica funcional (reglas de negocio) que permitirán analizar los datos y suministrar los
  resultados
- La lógica del modelo de datos (obtenida del archivo txt suministrado)
- El manejo de las excepciones en caso que el usuario coloque un archivo incorrecto de manera de facilitar el desarrollo de la aplicación, a continuación se le indica algunas instrucciones y clases y métodos que le podrían ser de utilidad.

### Instrucciones

Lee cuidadosamente todo el texto del proyecto antes de empezar a trabajar, si tiene alguna duda, consulte al profesor, según las condiciones al final del texto.

- Use una estructura de carpetas (paquetes) que permita la separación de las diferentes partes de la aplicación. Se sugiere una para la vista, otra para la parte de obtención de datos,una para el manejo de excepciones y una para su procesamiento (controlador).
- El archivo suministrado contiene en cada línea la siguiente información separada por comas:`Nro CI`, `1er Apellido`, `2do Apellido`, `Nombre`, `Inicial 2do Nombre`, `Sexo`, `Edad`, `Horas`,
  `Minutos` y `Segundos`.
- El archivo lo puede descargar desde el mismo módulo donde se publique este texto

### Requerimientos

- La ventana principal del proyecto debe contener un menú para manejar las opciones y acciones de la aplicación: `Archivo` y `Acciones`. Desde el menú `Archivo` se podrá Seleccionar `Cargar Archivo`, para escoger el archivo que contendrá los datos y `Salir`, para salirse de la aplicación.
En Acciones se mostrarán diversas acciones de acuerdo a lo que el usuario desee ver, de acuerdo a los resultados que se solicitan más abajo.

- Los resultados solicitados serán mostrados en dos maneras:
    - Si el resultado solicitado es de una línea, se presentará en una sola línea
    - Si el resultado involucra varios datos se debe presentar en una tabla formateada sobre la salida estándar, usando los comandos aprendidos en clase para el formateo de strings y el uso de print.
- Los participantes se dividen en grupos etarios (por edad) y por sexo. Los grupos etarios son:
    - `Juniors`, iguales o menores a 25 años,
    - `Seniors`, iguales o mayores de 25 y menores o iguales a 40 años y
    - `Masters`, mayores de 40 años
- Los resultados a mostrar, usando diversos menús de selección en la opción Acciones son:
    - Lista con la totalidad de participantes (tabla)
    - Cantidad total de participantes (una línea)
    - Cantidad de participantes por grupo etario (tabla, solo el grupo y la cantidad)
    - Cantidad de participantes por sexo (línea, sólo el grupo y la cantidad)
    - Ganadores por grupo etario (tabla)
    - Ganadores por sexo (tabla)
    - Ganadores por grupo etario y sexo (tabla)
    - Ganador general (línea)
    - Histograma de participante por grupo etario
    - Promedio de tiempo por grupo etario y sexo

- Se considera ganador al participante que ha empleado menos tiempo en ejecutar la competencia.

- Un histograma es un gráfico que se presentará de la manera siguiente:

```terminal
Juniors (x): | ***********
Masters (y): | ********************
Seniors (z): | ********
```

Donde `x`, `y` y `z` representan a la cantidad de participantes por grupo etario.

- Después de presentar cada acción del menú debe existir una opción para retornar al menú principal.
- La aplicación debe estar activa mientras el usuario no seleccione la opción de salir del menú
Archivos.

### Las excepciones y mensajes:
La aplicación debe ser capaz de suministrar información al usuario cuando cargue un archivo que no sea el correcto, es decir que no sea un archivo .txt. Las excepciones que debe manejar el sistema, con sus respectivos mensajes son:

- Tipo de archivo incorrecto (para validar que sea txt).
- Cantidad de columnas incorrecto (las líneas tienen la información indicada anteriormente).

Al producirse cualquier de los fallos mencionados debe notificar al usuario con un mensaje y permitiéndole repetir la acción de forma correcta.

### Archivo de prueba:
El archivo a usar para probar la aplicación se descargará del módulo 7 (nuevo), tiene por nombre `competencia.txt`. Su contenido está compuesto por una serie de líneas, las cuales representan los datos de un participante y están separados por coma (,) tal como se describió anteriormente.

### RECURSOS:
- La página https://docs.python.org/3/library/datetime.html posee información acerca del
procesamiento de los tiempos y otras librerías
- Otras páginas útiles para el manejo de los tiempos son:
    - https://www.programmiz.com/python-programming/datetime
    - https://www.w3schools.com/python/python_datetime.asp
    - https://www.geeksforgeeks.org/python-datetime-module/
    - https://realpython.com/python-datetime/
- Para el manejo de los prints (para formatear las listas) puede consultar:
    - https://realpython.com/python-print/

### CONDICIONES:
- La presentación del proyecto será individual.
- Se debe subir al sitio indicado en la pregunta respectiva del parcial en M7 el archivo con el
proyecto empaquetado en un archivo zip o rar.
- Se evaluará de la manera siguiente:
- Resultado, a partir del ejecutable entregado: 50%
- Organización y estilo del código, revisado en el proyecto: 30%
- Documentación del código, carpeta contentiva del API de la aplicación: 20%
- Los nombres de paquetes, módulos y variables a utilizar deben tener un nombre auto
explicativo y en inglés. La documentación del código puede estar en español.
- El sistema debe ser auto-explicativo en el sentido que no se necesite un manual para ejecutarlo y la obtención de resultados.