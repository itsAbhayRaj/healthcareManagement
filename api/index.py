from django.core.wsgi import get_wsgi_application
import os

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings.prod')

# Get the WSGI application
application = get_wsgi_application()
