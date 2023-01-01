# Proyecto: Proyecto Final con Django Coderhouse 34640
## Estudiante: Facundo Mercado
Proyecto Final para el curso de Coderhouse sobre Introduccion a Python

## Video demostrativo
>https://youtu.be/XdOiRegkVnU
>

### Casos de prueba

Al entrar al sitio, 
>http://127.0.0.1:8000/
>
Podremos ver la pagina de inicio del Blog. Como la mayor atracción de las paginas web estilo Blog es el contenido que sube su autor, nos vamos a dirigir
a la pestaña de "Articulos" dentro de la barra de navegacion, y luego en el menu que se abre haremos click en "Ver lista de articulos"

| Lo que se espera que suceda | Lo que sucede |
| ------------- | ------------- |
| Por cada articulo que el blog tenga creado, aparecera un apartado dentro de la pagina con el titulo del articulo, la fecha en que fue publicado, si tiene comentarios y cuantos tiene de ser el caso. Tambien aparecera una breve introduccion al articulo y un hipervinculo en forma de un "Leer más" |   Si, cumple |
| Al hacer click en "Leer más" desde la vista de lista de los articulos, nos debera llevar al articulo correspondiente. Aqui podremos ver el articulo en cuestion con mayor detalle, desbloqueando todo su contenido, como tambien la opcion de dejar un comentario | Si, cumple |
| Al intentar dejar un comentario sin tener una sesion iniciada, deberia rebotarnos con un mensaje en pantalla que diga "Debes iniciar sesion para dejar un comentario". | No, no cumple. Nos retorna un error de servidor. No logre capturar la clase AnonymousUser de manera que pueda evitar el error |
| Dirigiendonos a la pestaña Registro, crearemos un usuario. Se espera que al rellenar los campos de forma valida y hacer click en el boton de "Registrarse" se lleve a cabo la creacion del usuario sin inconveniente alguno. | Si, cumple|
| Una vez creado el usuario, nos dirigiremos a la opcion de iniciar sesion. Ingresando sin errores nuestras credenciales, deberiamos poder iniciar sesion en nuestra cuenta recien creada. | Si, cumple |
| En el extremo superior derecho, dentro de la barra de navegacion, ahora debería aparecer nuestro nombre de usuario. Al hacerle click, veremos una serie de opciones. Dentro de la opcion "Ver perfil" descubriremos una interfaz donde podemos cambiar nuestro nombre de usuario y nuestro mail, simplemente escribiendo uno nuevo o modificando el anterior. Al hacer click en "Actualizar usuario" deberiamos ver reflejados los cambios dentro de nuestro propio perfil. | Si, cumple |
| En las opciones del Perfil, nos dirigiremos hacia "Mensajes". Una vez ahi, deberiamos tener el inbox vacio, ya que todavia no hemos iniciado conversacion con nadie. Nos dirigimos hacia la URL con el proposito de cambiarla, y la editaremos de de manera que http://127.0.0.1:8000/ms/inbox pase a ser: http://127.0.0.1:8000/ms/(elnombredeunusuario) por ejemplo, escribiendo http://127.0.0.1:8000/ms/Apolo estaremos creando una nueva "Sala de chat" con el usuario "Apolo" | Si, cumple |
