from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from apps.student_data.models import StudentData
from .models import Document


@receiver(post_save, sender=Document)
def document_upload_notify(sender, instance, created, **kwargs):
    if created:
        try:
            managers_queryset = instance.student_data.user.managers.all()
        except StudentData.user.RelatedObjectDoesNotExist:
            return
        for manager in managers_queryset:
            notify.send(sender=instance.student_data.user, recipient=manager.manager, verb="uploaded",
                        action_object=instance, level="success", timestamp=instance.uploaded_at)
