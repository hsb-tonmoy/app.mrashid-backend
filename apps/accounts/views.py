from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings

from .models import Accounts
from .serializers import AccountsListSerializer, AccountsRetrieveSerializer, AccountsUpdateSerializer
from .permissions import OnlyAdminandStaffCanRetrieve

GOOGLE_OAUTH_CALLBACK_URL = settings.GOOGLE_OAUTH_CALLBACK_URL


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = GOOGLE_OAUTH_CALLBACK_URL
    client_class = OAuth2Client


class AccountsViewset(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsRetrieveSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated, OnlyAdminandStaffCanRetrieve]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email', ]
    lookup_field = 'username'
    list_serializer_class = AccountsListSerializer
    update_serializer_class = AccountsUpdateSerializer

    def get_serializer_class(self):

        if self.action == 'list':
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class

        elif self.action == 'update' or self.action == 'partial_update':
            if hasattr(self, 'update_serializer_class'):
                return self.update_serializer_class

        return super(AccountsViewset, self).get_serializer_class()
