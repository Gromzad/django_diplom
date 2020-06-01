"""
WSGI config for ToolProduction project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ToolProduction.settings")
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToolProduction.settings')

application = get_wsgi_application()
application = Cling(get_wsgi_application())
