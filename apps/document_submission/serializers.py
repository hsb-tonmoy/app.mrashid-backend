from rest_framework import serializers
from .models import Document, DocumentCategory


class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = "__all__"


class DocumentListSerializer(serializers.ModelSerializer):
    category = DocumentCategorySerializer()

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
