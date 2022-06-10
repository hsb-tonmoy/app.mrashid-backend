from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template
from post_office import mail
from .models import Note, PRIORITY_CHOICES


@receiver(post_save, sender=Note)
def send_welcome_email(sender, instance, created, **kwargs):

    if created and (instance.priority >= 3 and not instance.internal):

        priority = dict(PRIORITY_CHOICES).get(instance.priority)

        context = {
            'first_name': instance.student.first_name,
            'title': instance.title,
            'description': instance.description,
            'priority': priority,
        }

        template = get_template(
            'notes/notification-email.html').render(context)

        mail.send([instance.student.email], "Team Mrashid <team@mrashid.net>", subject=f"{instance.student.first_name}, you have a new notification!",
                  html_message=template, priority='now')
