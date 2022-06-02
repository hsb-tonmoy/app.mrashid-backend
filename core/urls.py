from django.contrib import admin
from django.conf import settings
from django.urls import re_path, path, include
from django.views.generic import RedirectView, TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from apps.accounts.views import FacebookLogin, GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.student_data.urls', namespace='student_data')),
    path('api/v1/', include('apps.accounts.urls', namespace='accounts')),
    path('api/v1/', include('apps.notes.urls', namespace='notes')),
    path('api/v1/', include('apps.document_submission.urls',
         namespace='document_submission')),
    path('api/v1/', include('apps.application_submission.urls',
         namespace='application_submission')),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path(r'^login/forgot/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
            TemplateView.as_view(template_name="password_reset_confirm.html"),
            name='password_reset_confirm'),
    path('api/v1/auth/', include('allauth.urls'), name='socialaccount_signup'),
    path('api/v1/auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api/v1/auth/google/', GoogleLogin.as_view(), name='google_login'),
    path("api/v1/messages-drf/", include("django_messages_drf.urls",
                                         namespace="django_messages_drf")),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
