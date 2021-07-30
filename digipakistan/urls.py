from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_auth.registration.views import VerifyEmailView, RegisterView
from allauth.account.views import ConfirmEmailView
from rest_auth.views import PasswordResetView, PasswordResetConfirmView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    #verify email
    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
         VerifyEmailView.as_view(), name='account_confirm_email'),

    #paswword reset
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),


    path('teacher/', include('teacherApp.urls')),
    path('product/', include('Product.urls')),
    path('superadmin/', include('superadmin.urls')),
    path('users/', include('auth_users.urls')),
    path('parent/', include('parentApp.urls')),
    path('administrator/', include('adminapp.urls')),
    path('student/', include('Student.urls')),
    path('client/', include('client.urls')),



    

]
#urlpatterns += [
#    path('api-auth/', include('rest_framework.urls'))
#]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# https://dev.to/jkaylight/django-rest-framework-authentication-with-dj-rest-auth-4kli
# https://dj-rest-auth.readthedocs.io/en/latest/faq.html
