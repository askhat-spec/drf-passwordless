from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'users'

urlpatterns = [
    path('otp/', SendOTPView.as_view(), name='otp'),
    path('token/', LoginOTPView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('test/', protected_view, name='protected-view')
]