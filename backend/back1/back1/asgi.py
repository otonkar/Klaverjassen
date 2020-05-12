"""
ASGI config for back1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import django

#from django.core.asgi import get_asgi_application
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back1.settings')

## Added extra
django.setup()

## https://stackoverflow.com/questions/59908273/django-daphne-asgi-django-can-only-handle-asgi-http-connections-not-websocket
#application = get_asgi_application()
application = get_default_application()
