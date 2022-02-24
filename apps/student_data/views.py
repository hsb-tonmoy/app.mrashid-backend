from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from .models import StudentData
from .serializers import StudentDataRetrieveSerializer, StudentDataListSerializer
from .permissions import StudentDataPermissions, OnlyOwnerandStaffCanRetrieve
from .pagination import StudentDataPagination


class StudentDataViewSet(viewsets.ModelViewSet):
    queryset = StudentData.objects.all()
    serializer_class = StudentDataRetrieveSerializer
    permission_classes = [StudentDataPermissions, OnlyOwnerandStaffCanRetrieve]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'social_media',
                     'destination', 'degree', 'major', 'english_proficiency', 'message']
    lookup_field = 'id'
    ordering = ['-rating', 'id']

    list_serializer_class = StudentDataListSerializer

    def get_serializer_class(self):

        if self.action == 'list':
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class

        return super(StudentDataViewSet, self).get_serializer_class()
