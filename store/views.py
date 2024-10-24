from rest_framework.permissions import AllowAny, IsAuthenticated  # NOQA
from rest_framework.viewsets import ModelViewSet

from .models import Author, Book, Publication
from .serializer import AuthorSerializer, BookReadSerializer, PublicationSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)


class PublicationViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = (AllowAny,)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookReadSerializer
    permission_classes = (AllowAny,)
