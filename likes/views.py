# Importing necessary Django REST framework classes and custom permissions
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer

# LikeList class for handling listing and creating likes
class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    This view handles GET requests to list all likes and POST requests to create a new like.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Permissions - allow any read actions but restrict write actions to authenticated users
    serializer_class = LikeSerializer  # Specifies the serializer to use for request/response data formatting
    queryset = Like.objects.all()  # The queryset representing the database query to be executed for likes

    def perform_create(self, serializer):
        """
        Custom method to associate the current user with a new like during creation.
        This is called when a new like is being created.
        """
        serializer.save(owner=self.request.user)  # Save the like instance with the owner field set to the currently authenticated user

# LikeDetail class for handling individual like retrieval and deletion
class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    This view handles GET requests for retrieving a like and DELETE requests for deleting a like.
    """
    permission_classes = [IsOwnerOrReadOnly]  # Custom permission - allows operations only if the user is the owner of the like
    serializer_class = LikeSerializer  # Specifies the serializer for like data
    queryset = Like.objects.all()  # The queryset for retrieving the like from the database
