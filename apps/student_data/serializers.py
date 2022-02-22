from rest_framework import serializers
from .models import StudentData


class StudentDataRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = "__all__"


class StudentDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = ('id', 'email', 'first_name', 'last_name', 'destination',
                  'degree', 'major', 'english_proficiency', 'created', 'status', 'rating')
