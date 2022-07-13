from django.apps import AppConfig


class DocumentSubmissionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.document_submission'

    def ready(self):
        from . import signals
