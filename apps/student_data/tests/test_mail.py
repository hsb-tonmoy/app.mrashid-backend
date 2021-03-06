from django.test import TestCase
from django.core import mail


class TestMail(TestCase):
    def test_send_mail(self):
        mail.send_mail(
            'Test Subject',
            'Here is the message body.',
            'no-reply@mrashid.net',
            ['to@example.com']
        )
        assert len(mail.outbox) == 1, "Inbox is not empty"
        assert mail.outbox[0].subject == 'Test Subject'
        assert mail.outbox[0].body == 'Here is the message body.'
        assert mail.outbox[0].from_email == 'no-reply@mrashid.net'
        assert mail.outbox[0].to == ['to@example.com']
