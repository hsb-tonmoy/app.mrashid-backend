from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentDataViewSet, send_student_email

app_name = 'apps.student_data'

router = DefaultRouter()

router.register(r'student_data', StudentDataViewSet, basename='student_data')

urlpatterns = [
    path('', include((router.urls))),
    path('send_email/', send_student_email, name='send_email'),
]
