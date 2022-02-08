from django.apps import AppConfig


class StudentDataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.student_data'

    def ready(self):
        from . import signals
