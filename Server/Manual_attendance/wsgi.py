import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Manual_attendance.Manual_attendance.settings')

application = get_wsgi_application()

