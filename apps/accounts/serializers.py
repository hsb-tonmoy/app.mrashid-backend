from dj_rest_auth.serializers import PasswordResetSerializer
from dj_rest_auth.forms import AllAuthPasswordResetForm
from allauth.utils import build_absolute_uri
from allauth.account.utils import user_pk_to_url_str, user_username
from allauth.account.adapter import get_adapter
from allauth.account import app_settings
from django.urls.base import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from notifications.models import Notification
from .models import Accounts, ClientFollowing
from apps.student_data.serializers import StudentDataListSerializer, StudentDataBriefSerializer

User = get_user_model()


class RegistrationSerializer(RegisterSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.save(update_fields=['first_name', 'last_name'])


class CustomUserDetailsSerializer(UserDetailsSerializer):
    profile_pic = serializers.ImageField()

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name',
                  'last_name', 'account_type', 'profile_pic', 'student_id')
        read_only_fields = ('email', 'username')


class AccountsBriefSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = Accounts
        fields = ('id', 'username', 'full_name', )


class AccountsListSerializer(serializers.ModelSerializer):
    student = StudentDataBriefSerializer()

    class Meta:
        model = Accounts
        exclude = ('password', )


class AccountsRetrieveSerializer(serializers.ModelSerializer):
    student = StudentDataListSerializer()

    class Meta:
        model = Accounts
        fields = "__all__"


class AccountsUpdateSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=False)

    # def create(self, validated_data):
    #     user = super(AccountsUpdateSerializer, self).create(validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    # def update(self, instance, validated_data):
    #     user = super(AccountsUpdateSerializer, self).update(
    #         instance, validated_data)
    #     if validated_data['password']:
    #         user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    class Meta:
        model = Accounts
        fields = "__all__"


'''

Custom Form and Serializer to override PasswordRest URL domain.

'''


class CustomAllAuthPasswordResetForm(AllAuthPasswordResetForm):
    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data['email']
        token_generator = kwargs.get('token_generator',
                                     default_token_generator)

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email
            path = reverse(
                'password_reset_confirm',
                args=[user_pk_to_url_str(user), temp_key],
            )
            # PASS NONE INSTEAD OF REQUEST
            url = build_absolute_uri(None, path)

            context = {
                'current_site': current_site,
                'user': user,
                'password_reset_url': url,
                'request': request,
            }
            if app_settings.AUTHENTICATION_METHOD != app_settings.AuthenticationMethod.EMAIL:
                context['username'] = user_username(user)
            get_adapter(request).send_mail('account/email/password_reset_key',
                                           email, context)
        return self.cleaned_data['email']


class CustomPasswordResetSerializer(PasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        return CustomAllAuthPasswordResetForm


class ClientFollowingSerializer(serializers.ModelSerializer):
    client = AccountsBriefSerializer()

    class Meta:
        model = ClientFollowing
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    actor = AccountsBriefSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'
