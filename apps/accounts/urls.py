from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AccountsViewset

app_name = 'apps.accounts'

router = DefaultRouter()

router.register(r'accounts', AccountsViewset, basename='accounts')

urlpatterns = [
    path('', include((router.urls))),
]
