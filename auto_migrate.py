# auto_migrate.py
import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # ← अपने प्रोजेक्ट के अनुसार बदलें
django.setup()
call_command('migrate')
