from rest_framework import serializers
from .models import StudentData, StudentProgress


class StudentProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProgress
        fields = "__all__"


class StudentDataRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentData
        fields = "__all__"


class StudentDataListSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source="user.username")

    class Meta:
        model = StudentData
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'destination',
                  'degree', 'major', 'english_proficiency', 'created', 'status', 'rating')
