from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template
from post_office import mail
from .models import StudentData
import time


@receiver(post_save, sender=StudentData)
def send_welcome_email(sender, instance, created, **kwargs):

    if created:

        context = {
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'date_time': time.strftime("%d %B %Y %I:%M %p"),
        }

        template = get_template(
            'student_data/welcome-email.html').render(context)

        mail.send([instance.email], subject="Welcome to app.mrashid.net",
                  html_message=template, priority='now')
