import os
import django

# Django settings configure करो
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # ← यहाँ अपने project का नाम भरो

# Django setup
django.setup()

from django.contrib.auth.models import User

# Check if superuser already exists
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
    print("✅ Superuser created successfully!")
else:
    print("ℹ️ Superuser already exists.")
