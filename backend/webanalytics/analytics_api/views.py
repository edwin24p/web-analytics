from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Even though we made password write only we pop it from the response just in case
        response= super().create(request, *args, **kwargs)
        response.data.pop("password", None)
        return response
    