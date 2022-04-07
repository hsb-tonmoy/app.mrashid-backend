from rest_framework import serializers
from apps.accounts.serializers import AccountsBriefSerializer
from apps.student_data.serializers import StudentDataBriefSerializer
from .models import Document, DocumentCategory


class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = "__all__"


class DocumentListSerializer(serializers.ModelSerializer):
    category = DocumentCategorySerializer()
    student_data = StudentDataBriefSerializer()
    checked_by = AccountsBriefSerializer()

    class Meta:
        model = Document
        fields = "__all__"


class DocumentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = "__all__"

    def to_representation(self, instance):
        serializer = DocumentListSerializer(instance)
        return serializer.data
