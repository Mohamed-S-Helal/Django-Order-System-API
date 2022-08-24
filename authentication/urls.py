from django.urls import path
from authentication.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'auth'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterView.as_view()),
]