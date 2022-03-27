from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PreApplicationForm
from .serializers import PreApplicationFormSerializer


class PreApplicationFormViewset(viewsets.ModelViewSet):
    queryset = PreApplicationForm.objects.all()
    serializer_class = PreApplicationFormSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'student__id'
