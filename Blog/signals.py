from django.db.models.signals import post_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver
from decouple import config

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    """
    Create a superuser after all migrations have run.
    """
    if not User.objects.filter(is_superuser=True).exists():
        username = config('SUPERUSER_NAME', default='admin')
        email = config('SUPERUSER_EMAIL', default='admin@example.com')
        password = config('SUPERUSER_PASSWORD', default='admin123')

        print(f"Creating default superuser '{username}'...")
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser created successfully.")
