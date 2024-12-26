"""
WSGI config for Fitnessclass_scheduler project.

It exposes the WSGI callable as a module-level variable named ``app``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Fitnessclass_scheduler.settings")

# Initialize the application
app = get_wsgi_application()

# Ensure the database is migrated and exists in a writable location (e.g., /tmp for Vercel)
db_path = "/tmp/db.sqlite3"

if not os.path.exists(db_path):
    from django.conf import settings
    settings.DATABASES["default"]["NAME"] = db_path  # Update the database path to /tmp
    call_command("migrate")

