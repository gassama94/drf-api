# Importing necessary modules and classes from Django REST framework and custom permissions
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

# FollowerList class for handling listing and creating followers
class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of a user
    following another user.
    Create a follower, i.e. follow a user if logged in.
    Perform_create: associate the current logged in user with a follower.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Permissions - allow any read actions but restrict write actions to authenticated users
    queryset = Follower.objects.all()  # The queryset representing the database query to be executed for followers
    serializer_class = FollowerSerializer  # Specifies the serializer to use for request/response data formatting

    def perform_create(self, serializer):
        """
        Custom method to associate the current user with a new follower during creation.
        This is called when a new follower instance is being created.
        """
        serializer.save(owner=self.request.user)  # Save the follower instance with the owner field set to the currently authenticated user

# FollowerDetail class for handling individual follower retrieval and deletion
class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower.
    No Update view, as we either follow or unfollow users.
    Destroy a follower, i.e., unfollow someone if owner.
    """
    permission_classes = [IsOwnerOrReadOnly]  # Custom permission - allows operations only if the user is the owner of the follower
    queryset = Follower.objects.all()  # The queryset for retrieving the follower from the database
    serializer_class = FollowerSerializer  # Specifies the serializer for follower data
