import os
from dotenv import load_dotenv
import django

# Load env
load_dotenv()

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

django.setup()

from django.contrib.auth.models import User

# Create superuser
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
    print("✅ Superuser created successfully!")
else:
    print("⚠️ Superuser already exists.")
