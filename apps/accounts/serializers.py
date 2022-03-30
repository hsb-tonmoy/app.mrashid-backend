from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Accounts
from apps.student_data.serializers import StudentDataListSerializer

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


class AccountsListSerializer(serializers.ModelSerializer):
    student = StudentDataListSerializer(read_only=True)

    class Meta:
        model = Accounts
        fields = ('id', 'email', 'username', 'profile_pic', 'first_name', 'last_name',
                  'is_staff', 'is_superuser', 'is_active', 'date_joined', 'account_type', 'student', 'last_login')


class AccountsRetrieveSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = super(AccountsRetrieveSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super(AccountsRetrieveSerializer, self).update(
            instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Accounts
        fields = "__all__"
