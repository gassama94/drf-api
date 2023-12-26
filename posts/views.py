# Import necessary modules and classes from Django REST framework and custom permissions
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

# PostList class for handling the listing and creation of posts
class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in.
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer  # Specifies the serializer to use for formatting request/response data
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Permissions - allow any read actions but restrict write actions to authenticated users
    queryset = Post.objects.all()  # The queryset representing the database query to be executed for posts

    def perform_create(self, serializer):
        """
        Custom method to associate the current user with a new post during creation.
        This is called when a new post is being created.
        """
        serializer.save(owner=self.request.user)  # Save the post instance with the owner field set to the currently authenticated user

# PostDetail class for handling the retrieval, update, and deletion of a specific post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer  # Specifies the serializer for post data
    permission_classes = [IsOwnerOrReadOnly]  # Custom permission - allows operations only if the user is the owner of the post
    queryset = Post.objects.all()  # The queryset for retrieving the post from the database
