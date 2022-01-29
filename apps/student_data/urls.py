from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentDataViewSet

app_name = 'apps.student_data'

router = DefaultRouter()

router.register(r'student_data', StudentDataViewSet, basename='student_data')

urlpatterns = [
    path('', include((router.urls))),
]
