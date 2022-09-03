from rest_framework import serializers
from apps.student_data.models import StudentData, StudentProgress


class HistoricalRecordField(serializers.ListField):
    child = serializers.DictField()

    def to_representation(self, data):
        return super().to_representation(data.values())


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

    history = serializers.SerializerMethodField()

    def get_history(self, obj):
        # using slicing to exclude current field values
        model_history = obj.history.filter(id=obj.pk).values(
            'history_date', 'history_user_id').order_by('-history_date').first()
        return model_history

    class Meta:
        model = StudentData
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'destination',
                  'degree', 'major', 'english_proficiency', 'created', 'status', 'rating', 'history')


class StudentDataBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentData
        fields = ('id', 'email', 'first_name', 'last_name',)
