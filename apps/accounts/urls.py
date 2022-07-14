from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AccountsViewset, ClientFollowingViewset, NotificationViewset

app_name = 'apps.accounts'

router = DefaultRouter()

router.register(r'accounts', AccountsViewset, basename='accounts')
router.register(r'clientfollowing', ClientFollowingViewset,
                basename='clientfollowing')
router.register(r'notifications', NotificationViewset,
                basename='notifications')

urlpatterns = [
    path('', include((router.urls))),
]
