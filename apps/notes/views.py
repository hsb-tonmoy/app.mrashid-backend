from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import NoteListSerializer, NoteCreateSerializer, NoteCategorySerializer
from .models import Note, NoteCategory


class NoteCategoryViewset(viewsets.ModelViewSet):
    queryset = NoteCategory.objects.all()
    serializer_class = NoteCategorySerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteCreateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student', 'internal', 'priority', 'category']

    list_serializer_class = NoteListSerializer

    def get_serializer_class(self):

        if self.action == 'list':
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class

        return super(NoteViewSet, self).get_serializer_class()
