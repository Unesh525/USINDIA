# auto_migrate.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # अपना project name दो
django.setup()

from django.core.management import call_command

call_command("migrate")
