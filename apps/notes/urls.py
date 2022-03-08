from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteCategoryViewset, NoteViewSet

app_name = 'apps.notes'

router = DefaultRouter()

router.register(r'note_category', NoteCategoryViewset,
                basename='note_category')
router.register(r'note', NoteViewSet, basename='note')

urlpatterns = [
    path('', include((router.urls))),
]
