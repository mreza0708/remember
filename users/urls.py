from django.urls import path
from users.views import RegisterView, LoginView, UserProfileView, SendEmailAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('send-email/', SendEmailAPIView.as_view(), name='send-email'),  # optional
]
