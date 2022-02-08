from django.core.management.base import BaseCommand
from django.template.loader import get_template
from post_office import mail
import datetime
import pytz


class Command(BaseCommand):
    def handle(self, *args, **options):
        current_time = datetime.datetime.now()

        current_time = current_time.astimezone(
            pytz.timezone('US/Eastern')).strftime('%d %B %Y %I:%M %p')

        context = {
            'first_name': 'app.mrashid',
            'last_name': '.net',
            'date_time': current_time,
        }

        template = get_template(
            'student_data/welcome-email.html').render(context)

        mail.send(['hello@mrashid.net'], "Mamoon Rashid <no-reply@mrashid.net>", subject="Welcome to app.mrashid.net",
                  html_message=template, priority='now')
