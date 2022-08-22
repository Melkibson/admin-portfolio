"""
WSGI config for admin_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from whois import whois
from admin_portfolio.asgi import application as asgi_application
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_portfolio.settings')

try:
    whois('127.0.0.1')
    application = get_wsgi_application()
except Exception as e:
    print(e)
else:
    app = asgi_application


