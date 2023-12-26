# Importing necessary classes and functions from Django REST framework and local modules
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

# CommentList class-based view to handle the listing and creation of comments
class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    This view handles GET requests to list all comments and POST requests to create a new comment.
    """
    serializer_class = CommentSerializer  # Specifies the serializer to use for formatting request/response data
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Permissions - allow any read actions but restrict write actions to authenticated users
    queryset = Comment.objects.all()  # The queryset that represents the database query to be executed

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']


    def perform_create(self, serializer):
        """
        Custom method to associate the current user with a new comment during creation.
        This is called when a new comment is being created.
        """
        serializer.save(owner=self.request.user)  # Save the comment instance with the owner field set to the currently authenticated user

# CommentDetail class-based view for retrieving, updating, and deleting a specific comment
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific comment.
    This view handles GET requests to retrieve a comment, PUT/PATCH requests to update a comment, and DELETE requests to delete a comment.
    """
    permission_classes = [IsOwnerOrReadOnly]  # Custom permission - allows operations only if the user is the owner of the comment
    serializer_class = CommentDetailSerializer  # Specifies the serializer for detailed comment data
    queryset = Comment.objects.all()  # The queryset for retrieving the comment from the database
