from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DocumentCategoryViewset, DocumentViewset

app_name = 'apps.document_submission'

router = DefaultRouter()

router.register(r'document_category', DocumentCategoryViewset,
                basename='note_category')
router.register(r'document', DocumentViewset, basename='document')

urlpatterns = [
    path('', include((router.urls))),
]
