from rest_framework import viewsets

from .models import StudentData
from .serializers import StudentDataRetrieveSerializer, StudentDataListSerializer
from .permissions import StudentDataPermissions, OnlyOwnerandStaffCanRetrieve


class StudentDataViewSet(viewsets.ModelViewSet):
    queryset = StudentData.objects.all()
    serializer_class = StudentDataRetrieveSerializer
    permission_classes = [StudentDataPermissions, OnlyOwnerandStaffCanRetrieve]
    lookup_field = "user__username"

    list_serializer_class = StudentDataListSerializer

    def get_serializer_class(self):

        if self.action == 'list':
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class

        return super(StudentDataViewSet, self).get_serializer_class()
