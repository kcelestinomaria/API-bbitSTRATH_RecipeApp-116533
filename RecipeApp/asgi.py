"""
ASGI config for RecipeApp project.

Is the standard for Python asynchronous web apps
and servers to communicate with each other.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RecipeApp.settings')

application = get_asgi_application()
