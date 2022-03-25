from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

ACCOUNT_EMAIL_CONFIRMATION_URL = settings.ACCOUNT_EMAIL_CONFIRMATION_URL


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        url = ACCOUNT_EMAIL_CONFIRMATION_URL + emailconfirmation.key
        return url
