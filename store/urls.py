from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"", AuthorViewSet, basename="author")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
