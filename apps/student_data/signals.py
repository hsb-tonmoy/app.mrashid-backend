from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template
from post_office import mail
from .models import StudentData, StudentProgress
import datetime
import pytz
import sys


@receiver(post_save, sender=StudentData)
def create_student_progress(sender, instance, created, **kwargs):
    if created:
        student_progress = StudentProgress(
            student_data=instance, account_creation=2)
        student_progress.save()


@receiver(post_save, sender=StudentData)
def send_welcome_email(sender, instance, created, **kwargs):

    if created and not (len(sys.argv) > 1 and sys.argv[1] == 'runserver'):

        current_time = datetime.datetime.now()

        current_time = current_time.astimezone(
            pytz.timezone('US/Eastern')).strftime('%d %B %Y %I:%M %p')

        context = {
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'date_time': current_time,
        }

        template = get_template(
            'student_data/welcome-email.html').render(context)

        mail.send([instance.email], "Mamoon Rashid <no-reply@mrashid.net>", subject="Welcome to app.mrashid.net",
                  html_message=template, priority='now')
