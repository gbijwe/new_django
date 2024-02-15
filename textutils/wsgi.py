"""
WSGI config for textutils project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# import os

# postgresql://postgres:65CF4E516-dBe2D2dfD3Feb62c4cA42b@monorail.proxy.rlwy.net:39594/railway

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "textutils.settings")

# application = get_wsgi_application()

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings")
application = get_wsgi_application()
app = application