from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blog'

    def ready(self):
        import Blog.signals  # Ensure signals are loaded
