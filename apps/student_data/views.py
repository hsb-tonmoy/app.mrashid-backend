from rest_framework import viewsets

from .models import StudentData
from .serializers import StudentDataSerializer
from .permissions import StudentDataPermissions


class StudentDataViewSet(viewsets.ModelViewSet):
    queryset = StudentData.objects.all()
    serializer_class = StudentDataSerializer
    permission_classes = [StudentDataPermissions]
