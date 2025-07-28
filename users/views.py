from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import RegisterSerializer, LoginSerializer, UserProfileSerializer


def get_token_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    def post(self, request , *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(get_token_for_user(user), status=status.HTTP_201_CREATED)
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request , *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(get_token_for_user(user), status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_email_task  # import your celery task
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class SendEmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            subject = request.data.get("subject", "Test Subject")
            message = request.data.get("message", "This is a test email.")
            recipient = request.data.get("recipient", "mrezaheydari.0708@gmail.com")  # fallback test email

            send_email_task.delay(subject, message, settings.EMAIL_HOST_USER, [recipient])
            return Response({"message": "Email task sent to Celery!"}, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error("Send email error", exc_info=True)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
