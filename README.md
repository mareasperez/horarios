# Django Rest Api For University Schedules

Esta es una app de ejemplo en la que se usa
[Django](https://www.djangoproject.com/) para hacerla mas fácil de construir.
[Django-Rest-Framework](https://www.django-rest-framework.org/) para tener todas las funcionalidades de REST en nuestra app.
[Django-Channels](https://channels.readthedocs.io/en/latest/) para tener funcionalidades de los WebSockets e implementar comunicación en tiempo real entre los múltiples usuarios del app.

**Este App fue escrita con Django 2.2.1.
[example](https://gitlab.com/mareasperez7/horarios).**


Ejecutar esta aplicación en su máquina local en desarrollo funcionará
bien, Aunque necesitas instalar todos los requisitos:
## 1- Python (MiniConda)
En mi Caso yo utilizare [*MiniConda*](https://hcosta.github.io/instalardjango.com/) como gestor de entornos virtuales pero tambien se puede usar VirtualEnv eso es gusto de cada quien.  
## 2- Servidor PostgreSql
En este requisito es necesario tener un usuario y una base de datos sobre la cual se pueda trabajar con django si no tienes una puedes seguir el siguiente ejemplo para tener una base de datos local:
<br>
[Ubuntu](https://medium.com/crehana/creaci%C3%B3n-de-usuario-en-postgresql-10-4-y-ubuntu-18-04-9e80fe077f7e) 
<br>
[Windows](https://parzibyte.me/blog/2019/04/05/instalar-postgresql-11-windows/)
<br>

También se puede tener una base de datos remota ya que por de debajo solo se realizan peticiones a un motor de base de datos así que no importa si esta en nuestra maquina local o una nube un ejemplo para tener una DB remota podria ser usar [ElephantSql]({[https://www.elephantsql.com/](https://www.elephantsql.com/)})  que solamente tendriamos que crearnos una cuenta y ya podriamos crearnos una base de datos remota y de manera gratuita, obviamente con sus limitaciones.
## 3- Requirements.txt
Una vez teniendo [PostrgeSql](https://gitlab.com/mareasperez7/horarios/edit/master/README.md#2-servidor-postgresql) y Python instalados procederemos a instalar los modulos que python necesita para ejecutar el app.
##### Dentro de la carpeta del proyecto ejecutamos:
```sh
$ pip install -r Requirements.txt
```




## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv-2.7 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. Alternatively you
can use foreman and gunicorn to run the server locally (after copying
`dev.env` to `.env`):

```sh
$ foreman start
```

## Deploy to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/memcachier/examples-django.git
$ cd examples-django
$ heroku create
$ heroku addons:add memcachier:dev
$ git push heroku master:master
$ heroku open
```

## requirements.txt

MemCachier has been tested with the pylibmc memcache client, but the
default client doesn't support SASL authentication. Run the following
commands to install the necessary pips:

```sh
$ sudo brew install libmemcached
$ pip install django-pylibmc pylibmc
```

Don't forget to update your requirements.txt file with these new pips.
requirements.txt should have the following two lines:

```
django-pylibmc==0.6.1
pylibmc==1.5.1
```

## Configuring MemCachier (settings.py)

To configure Django to use pylibmc with SASL authentication. You'll also need
to setup your environment, because pylibmc expects different environment
variables than MemCachier provides. Somewhere in your `settings.py` file you
should have the following lines:

```python
os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

CACHES = {
    'default': {
        # Use pylibmc
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',

        # Use binary memcache protocol (needed for authentication)
        'BINARY': True,

        # TIMEOUT is not the connection timeout! It's the default expiration
        # timeout that should be applied to keys! Setting it to `None`
        # disables expiration.
        'TIMEOUT': None,
        'OPTIONS': {
            # Enable faster IO
            'tcp_nodelay': True,

            # Keep connection alive
            'tcp_keepalive': True,

            # Timeout settings
            'connect_timeout': 2000, # ms
            'send_timeout': 750 * 1000, # us
            'receive_timeout': 750 * 1000, # us
            '_poll_timeout': 2000, # ms

            # Better failover
            'ketama': True,
            'remove_failed': 1,
            'retry_timeout': 2,
            'dead_timeout': 30,
        }
    }
}
```

## Persistent Connections

By default, Django doesn't use persistent connections with memcached. This is a
huge performance problem, especially when using SASL authentication as the
connection setup is even more expensive than normal.

You can fix this by putting the following code in your `wsgi.py` file:

```python
# Fix django closing connection to MemCachier after every request (#11331)
from django.core.cache.backends.memcached import BaseMemcachedCache
BaseMemcachedCache.close = lambda self, **kwargs: None
```

There is a bug file against Django for this issue
([#11331](https://code.djangoproject.com/ticket/11331)).

## Application Code

In your application, use django.core.cache methods to access
MemCachier. A description of the low-level caching API can be found
[here](https://docs.djangoproject.com/en/1.8/topics/cache/#the-low-level-cache-api).
All the built-in Django caching tools will work, too.

Take a look at
[memcachier_algebra/views.py](https://github.com/memcachier/examples-django/blob/master/memcachier_algebra/views.py)
in this repository for an example.

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](http://github.com/memcachier/examples-django/issues).

Master [git repository](http://github.com/memcachier/examples-django):

* `git clone git://github.com/memcachier/examples-django.git`

## Licensing

This library is BSD-licensed.