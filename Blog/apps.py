from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth.models import User
from django.db.utils import OperationalError
from decouple import config

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blog'

    def ready(self):
        """
        Automatically create a superuser if none exists,
        using environment variables for credentials.
        """
        if not settings.DEBUG:  # Only in production
            try:
                if not User.objects.filter(is_superuser=True).exists():
                    username = config('SUPERUSER_NAME', default='admin')
                    email = config('SUPERUSER_EMAIL', default='admin@example.com')
                    password = config('SUPERUSER_PASSWORD', default='admin123')

                    print(f"Creating default superuser '{username}'...")
                    User.objects.create_superuser(username=username, email=email, password=password)
                    print("Default superuser created.")
            except OperationalError:
                # Happens when migrations aren't ready yet
                print("Skipping superuser creation, database not ready.")
