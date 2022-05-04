from django.urls import path, re_path, include
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.registration.views import ConfirmEmailView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
            ConfirmEmailView.as_view(), name='account_confirm_email',),
    path('account-email-verification-sent/', ConfirmEmailView.as_view(),
         name='account_email_verification_sent',),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
