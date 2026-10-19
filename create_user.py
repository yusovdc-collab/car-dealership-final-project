import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "dealership_project.settings"
)

django.setup()

from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

print("Starting Django user setup...", flush=True)

username = os.environ.get("DJANGO_ADMIN_USERNAME")
password = os.environ.get("DJANGO_ADMIN_PASSWORD")

if not username or not password:
    raise RuntimeError(
        "DJANGO_ADMIN_USERNAME or DJANGO_ADMIN_PASSWORD "
        "is missing from Render environment variables."
    )

user, created = User.objects.get_or_create(
    username=username
)

user.set_password(password)
user.is_active = True
user.is_staff = True
user.is_superuser = True
user.save()

if created:
    print("Django admin user created successfully.", flush=True)
else:
    print("Django admin user updated successfully.", flush=True)

authenticated_user = authenticate(
    username=username,
    password=password
)

if authenticated_user is None:
    raise RuntimeError(
        "Django authentication verification failed."
    )

print(
    "Django authentication verification successful.",
    flush=True
)