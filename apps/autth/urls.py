
from django.urls import path
from apps.autth.views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('pass/', UserChangePasswordView.as_view(), name='pass'),
    path('send-reset-password/', SendPasswordResetEmailView.as_view(), name='send-reset-password'),
    path('reset-password/<str:uidb64>/<str:token>/', UserPasswordResetView.as_view(), name='password-reset'),
    #path('reset-password/<uidb64>/<token>/', UserPasswordResetView.as_view(), name='password-reset'),
]