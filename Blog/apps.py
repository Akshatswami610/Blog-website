from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blog'

    def ready(self):
        # Auto-create superuser if none exists
        try:
            User = get_user_model()
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(
                    username='Akshat',
                    email='akshatswami0610@gmail.com',
                    password='123'
                )
                print("Superuser created: Akshat / 123")
        except OperationalError:
            # Database might not be ready on first run
            pass
