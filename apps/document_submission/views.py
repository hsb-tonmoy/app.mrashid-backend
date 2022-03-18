from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Document, DocumentCategory
from .serializers import DocumentCategorySerializer, DocumentListSerializer, DocumentCreateSerializer


class DocumentCategoryViewset(viewsets.ModelViewSet):
    queryset = DocumentCategory.objects.all()
    serializer_class = DocumentCategorySerializer


class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentCreateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_data', 'category__slug',
                        'is_approved', 'is_rejected', 'checked_by']

    list_serializer_class = DocumentListSerializer

    def get_serializer_class(self):

        if self.action == 'list':
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class

        return super(DocumentViewset, self).get_serializer_class()
