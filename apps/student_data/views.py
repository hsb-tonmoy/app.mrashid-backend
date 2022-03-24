from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import LimitOffsetPagination
from django.template.loader import get_template
from post_office import mail
from .models import StudentData, StudentProgress
from .serializers import StudentDataRetrieveSerializer, StudentDataListSerializer, StudentProgressSerializer
from .permissions import StudentDataPermissions, OnlyOwnerandStaffCanRetrieve


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


class StudentProgressViewset(viewsets.ModelViewSet):
    queryset = StudentProgress.objects.all()
    serializer_class = StudentProgressSerializer
    lookup_field = 'student_data__id'


@api_view(['POST'])
@permission_classes([IsAdminUser])
def send_student_email(request):
    if request.query_params:
        data_id = request.query_params.get('id')
    else:
        return Response({"error": "Please provide the user ID"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        data = StudentData.objects.get(id=data_id)
    except StudentData.DoesNotExist:
        return Response({"error": "Data does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    if request.data:
        try:
            subject = request.data['subject']
            message = request.data['message']
        except KeyError:
            return Response({"error": "Please provide the subject and the message"}, status=status.HTTP_400_BAD_REQUEST)

        context = {
            'first_name': data.first_name,
            'last_name': data.last_name,
            'message': message,
        }

        template = get_template(
            'student_data/student_custom_email.html').render(context)

        try:

            mail.send([data.email], "Mamoon Rashid <no-reply@mrashid.net>", subject=subject,
                      html_message=template, priority='now')
        except Exception:
            return Response({"error": "Email delivery unsuccessful"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"subject": subject, "message": message}, status=status.HTTP_200_OK)
