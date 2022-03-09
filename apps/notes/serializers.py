from rest_framework import serializers
from apps.accounts.serializers import CustomUserDetailsSerializer
from .models import Note, NoteCategory


class NoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteCategory
        fields = "__all__"


class NoteSerializer(serializers.ModelSerializer):
    category = NoteCategorySerializer(read_only=False)
    created_by = CustomUserDetailsSerializer(read_only=True)

    class Meta:
        model = Note
        fields = "__all__"
