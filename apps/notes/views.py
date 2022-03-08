from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import NoteSerializer, NoteCategorySerializer
from .models import Note, NoteCategory


class NoteCategoryViewset(viewsets.ModelViewSet):
    queryset = NoteCategory.objects.all()
    serializer_class = NoteCategorySerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student', 'internal', 'priority', 'category']
