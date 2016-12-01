import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "digital_animals.settings.development"
)

application = get_wsgi_application()
