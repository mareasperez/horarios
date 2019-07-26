# Api Rest en Django Para la creacion y gestion de Horarios.

Esta es una app de ejemplo en la que se usa:

[Django](https://www.djangoproject.com/) para hacerla mas fácil de construir.

[Django-Rest-Framework](https://www.django-rest-framework.org/) para tener todas las funcionalidades de REST en nuestra app.

[Django-Channels](https://channels.readthedocs.io/en/latest/) para tener funcionalidades de los WebSockets e implementar comunicación en tiempo real entre los múltiples usuarios del app.

[MiniConda](https://docs.conda.io/en/latest/miniconda.html) como gestor de entornos virtuales en reemplazo al clasico `Virtualenv`

**Este App fue escrita con Django 2.2.1.
[example](https://gitlab.com/mareasperez7/horarios).**


Ejecutar esta aplicación en su máquina local en desarrollo funcionará
bien, Aunque necesitas instalar todos los requisitos:
## 1- Python (MiniConda)
En mi Caso yo utilizare [*MiniConda*](https://hcosta.github.io/instalardjango.com/) como gestor de entornos virtuales pero tambien se puede usar `VirtualEnv` eso es gusto de cada quien.  
## 2- Servidor PostgreSql
En este requisito es necesario tener un usuario y una base de datos sobre la cual se pueda trabajar con django si no tienes una puedes seguir el siguiente ejemplo para tener una base de datos local:

[Ubuntu](https://medium.com/crehana/creaci%C3%B3n-de-usuario-en-postgresql-10-4-y-ubuntu-18-04-9e80fe077f7e) 

[Windows](https://parzibyte.me/blog/2019/04/05/instalar-postgresql-11-windows/)


También se puede tener una base de datos remota ya que por de debajo solo se realizan peticiones a un motor de base de datos así que no importa si esta en nuestra maquina local o una nube un ejemplo para tener una DB remota podria ser usar:

[ElephantSql](https://www.elephantsql.com/) 

Que solamente tendriamos que crearnos una cuenta y ya podriamos crearnos una base de datos remota y de manera gratuita, obviamente con sus limitaciones.
## 3- Requirements.txt
Una vez teniendo [PostrgeSql](https://gitlab.com/mareasperez7/horarios/blob/master/README.md#3-requirementstxt) y [ Python](https://gitlab.com/mareasperez7/horarios/blob/master/README.md#1-python-miniconda) instalados procederemos a instalar los módulos que python necesita para ejecutar el app para ello lo haremos dentro de un entorno virtual.
### Entorno Virtual

  
Es mejor usar la herramienta `miniconda` de python para compilar locamente:

```sh
$ conda create -n NombreEntorno python==XXX
```
Donde `XXX` es la versión de python que se utilizara. El comando quedaría así:

```sh
$ conda create -n Test python==3.7.3
```

luego toca activar nuestro entorno virtual con el siguiente comando:

```sh
$ conda activate Test
```

una vez teniendo el entorno activado se procede a instalar los requisitos.

##### Dentro de la carpeta del proyecto ejecutamos:

```sh
(Test)$ pip install -r Requirements.txt
```

#### Building

Una vez instalados todos los módulos. 
Antes de migrar los datos primero sera necesario configurar el archivo de configuracion `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Nombre de la Database',
        'USER': 'Usuario de la Database',
        'PASSWORD': 'Contrase;a de la DB',
        'HOST': 'Ubicacion del Servidor',
        'PORT': 'Puerto del servidor',
    }
}
``` 

Un ejemplo podria ser:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'horariosdb',
        'USER': 'usuario',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Procedemos a migrar los modelos a la base de datos para asi ya poder ejecutar el servidor.

```sh
(Test)$ python manage.py migrate
```

#### Creacion de SuperUsuario

La creacion del super usuario es necesaria para realizar la autenticacion ante el Servidor y asi este nos responda.

```sh
(Test)$ python manage.py createsuperuser
```

#### Puesta en marcha

Para arrancar el servidor de desarrollo de Django basta con ejecutar:

```sh
(Test)$ python manage.py runserver
```


## Licensing