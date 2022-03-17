from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Document, DocumentCategory
from .serializers import DocumentCategorySerializer, DocumentSerializer


class DocumentCategoryViewset(viewsets.ModelViewSet):
    queryset = DocumentCategory.objects.all()
    serializer_class = DocumentCategorySerializer


class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_data', 'category__slug',
                        'is_approved', 'is_rejected', 'checked_by']
