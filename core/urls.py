from django.contrib import admin
from django.urls import path, include

from apps.accounts.views import FacebookLogin, GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.student_data.urls', namespace='student_data')),
    path('api/v1/', include('apps.notes.urls', namespace='notes')),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/v1/auth/', include('allauth.urls'), name='socialaccount_signup'),
    path('api/v1/auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api/v1/auth/google/', GoogleLogin.as_view(), name='google_login')
]
