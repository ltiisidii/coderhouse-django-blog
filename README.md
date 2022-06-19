# CoderHousePython

## Entrega Final

### Integrantes 

Jonatan W

### Casos de prueba

[Link a drive ](https://docs.google.com/spreadsheets/d/1OYS7iVZuy_dkSCIztWNZG1nNKS8MnjT4/edit?usp=sharing&ouid=107614986716728974196&rtpof=true&sd=true)

### Link a Heroku

[Link](https://blog.appspot.cc/)

### Descripcion de tareas:

Realice la construccion completa del trabajo final utilizando Django, como hosting Heroku (PostgreSQL+Archivos Estaticos) y Cloudinary (avatar+media)

### Consigna: 

El objetivo es que cada estudiante pueda utulizar su proyecto final como parte de su portfolio personal.
Esta web tendra admin, perfiles, registro de usuario, paginas y formularios

- Registro de usuarios: 
    * Login/Signup
    * Reset pwd
    * Logout
- Paginas:
    * CRUD solo si esta registrado
- Perfil:
    * Imagen
    * Editar email/pwd
- Admin:
    * Apps

Dentro del github debera existir una carpeta con por lo menos 3 casos de pruebas debidamente documentados

Contar con algun acceso visible a la vista de "Acerca de mi" donde se contara acerca de los dueños de la pagia manejado en el route about/ (Que hable un poco de los creadores de la web y del proyecto)

Contar con algun acceso visible a la vista de blogs que debe alojarse en el route pages/ (Es decir un html que permite listar todos los blogs de la DB, con una informacion minima de dicho blog)

Acceder a una plantalla que contendra las pagina, al Clickear en "Leer mas" debe navegar al detalle de la page mediante un route pages/<pageId> (o sea al hacer click se ve mas detalle de lo que se veia en el apartado anterior)

Si no existe ninguna pagina mostrar un "No hay paginas aun" (Aclarando, si en una pagina hacemos click en algun lugar que no existe que diga eso, o que lleve a un html con esos mensajes, no dejar botones que no responden)

Para crear, editar o borrar las fotos debes estar registrado como Administrador

Cada blog, es decir cada model Blog debe tener como minimo: un titulo, subtitulo, cuerpo, autor, fecha y una imagen (minimo y obligatorio, puede tener mas)

Piezas sugeridas, no hace falta que esten todas, pero tiene que haber por lo menos un CRUD completo y el modulo de Login debe ser solido:

    * NavBar
    * Home
    * About
    * Pages
    * Login
    * Signup

    * Messages
    * Profile
    * Logout
    * Get Pages
    * Get page

    * Create page
    * Update page
    * Delete page
    * Get profile
    * Update profile


## Rutas

Inicio: al momento de ingresar a la app en la ruta base '/'

Visualizar el home del blog

## Diseño

Poder listar todas las paginas del blog, poder ver en detalle cada una, poder crear, editar o borrar paginas del blog

Las paginas estan formadas por un titulo, un contenido, un editor de texto avanzado (ckeditor por ejemplo), una imagen, fecha del posteo de la imagen

## APPS:

Tener una app de registro donde se puedan registrar usuarios en el route accounts/signup, un usuario esta compuesto por: email - contraseña - nombre de usuario

Tener una app de login en el route accounts/login/ la cual permite logearse con los datos de administrador o de usuario normal

Tener una app de perfiles en el route accounts/profile/ la cual muestra la info de nuestro usuario y permite modificar y/o borrar: imagen - nombre - descripcion - un link a una pagina web - email y contraseña

## Admin

Contar con un admin en el route admin/ donde se puedan manejar las apps y los datos en las apps.

Tener una app de mensajeria en el route messages/ para que los perfiles se puedan contactar entre si. 

*NOTA*: no hace falta que sean APPs separadas, con dos APP estaran bien.

## Pro Coders

Los requisitos extra pro-coders no se incluyen en los criterios de evaluacion

Los requisitos extra son funcionalidades opcionales que no se incluyen en los criterios de evaluacion, pero si te falta diversion y quieres agregar valor a tu proyecto... !bajo la unica condicion de que lo que incluyas debe funcionar!

    * Messenger y Like - Integracion con otra db
    * Subida a un servidor

## NO ES NECESARIO NI RECOMENDADO: 
    
    * Utilizar python puro para el proyecto final (se espera el uso de Django)

### Video acerca del funcionamiento de funcionamiento de la web

[![Ver el video](https://i.imgur.com/DrcBOej.png)](https://www.youtube.com/watch?v=bjnPIGNMApw)

