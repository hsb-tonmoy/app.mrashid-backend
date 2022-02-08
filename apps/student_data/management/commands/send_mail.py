from django.core.management import BaseCommand
from django.template.loader import get_template
from post_office import mail

import time


class Command(BaseCommand):
    help = "Send email"

    def handle(self, *args, **kwargs):
        # context = {
        #     'first_name': "Hasibuzzaman",
        #     'last_name': "Tonmoy",
        #     'date': time.strftime("%d %B %Y %x"),
        #     'time': time.strftime("%H:%M"),
        # }
        # template = get_template(
        #     'student_data/welcome-email.html').render(context)

        # mail.send(
        #     ['sirdarknight1366@gmail.com'],
        #     'no-reply@mrashid.net',
        #     html_message=template,
        #     priority='now',
        # )

        print(time.strftime("%d %B %Y %I:%M %p"))
