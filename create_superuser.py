import os
import django
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
    print("✅ Superuser created successfully!")
else:
    print("ℹ️ Superuser already exists.")
