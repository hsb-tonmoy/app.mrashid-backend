from django.test import TestCase
from django.core.mail import send_mail, outbox

import time


class TestMail(TestCase):
    def test_send_mail(self):
        send_mail(
            'Test Subject',
            'Here is the message body.',
            'no-reply@engmedapp.com',
            ['to@example.com']
        )
        assert len(outbox) == 1, "Inbox is not empty"
        assert outbox[0].subject == 'Test Subject'
        assert outbox[0].body == 'Here is the message body.'
        assert outbox[0].from_email == 'no-reply@engmedapp.com'
        assert outbox[0].to == ['to@example.com']
