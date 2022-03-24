from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

CALLBACK_URL_YOU_SET_ON_GOOGLE = 'http://localhost:3000/login/google'


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = CALLBACK_URL_YOU_SET_ON_GOOGLE
    client_class = OAuth2Client
