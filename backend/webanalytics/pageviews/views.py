from rest_framework.generics import CreateAPIView

from .models import PageView
from .serializers import PageViewSerializer


class PageViewCreateView(CreateAPIView):
    queryset=PageView.objects.all()
    serializer_class=PageViewSerializer
    authentication_classes = []

    def perform_create(self, serializer):
        """Retrieve ip address and user agent from client."""
        ip = self.request.META.get('REMOTE_ADDR')
        user_agent = self.request.META.get('HTTP_USER_AGENT', '')
        serializer.save(ip_address=ip, user_agent=user_agent)
