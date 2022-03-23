from rest_framework import serializers
from apps.accounts.serializers import CustomUserDetailsSerializer
from .models import Note, NoteCategory


class NoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteCategory
        fields = "__all__"


class NoteListSerializer(serializers.ModelSerializer):
    category = NoteCategorySerializer(read_only=False)
    created_by = CustomUserDetailsSerializer(read_only=True)

    class Meta:
        model = Note
        fields = "__all__"


class NoteCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Note
        fields = ('student', 'title', 'description', 'category',
                  'internal', 'complete', 'date_modified', 'priority', 'date_added', 'created_by')

    def to_representation(self, instance):
        serializer = NoteListSerializer(instance)
        return serializer.data
