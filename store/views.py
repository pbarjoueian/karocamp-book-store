from rest_framework.permissions import AllowAny, IsAuthenticated  # NOQA
from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializer import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.none()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)
