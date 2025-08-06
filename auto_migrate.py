import os
import django

# यह फ़ाइल बनाएंगे जब पहली बार migrate हो जाए
MIGRATION_FLAG = "migrated.txt"

if not os.path.exists(MIGRATION_FLAG):
    print("🔁 Running initial migrations...")
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # ← यहाँ अपना project name लिखो
    django.setup()

    from django.core.management import call_command
    call_command("migrate")

    # फ़ाइल create करो ताकि पता चले कि migration हो चुका है
    with open(MIGRATION_FLAG, "w") as f:
        f.write("Migrations done.")

    print("✅ Migrations completed and flag file created.")
else:
    print("⏭️ Migrations already done. Skipping.")
