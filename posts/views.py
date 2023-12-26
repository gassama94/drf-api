# Import necessary modules and classes from Django REST framework and custom permissions
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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

    # Using Django's annotate to add additional fields to the queryset.
    # These annotations are used to count related objects.
    queryset = Post.objects.annotate(
    # Counting the number of likes related to the object, ensuring each like is counted only once.
    likes_count=Count('likes', distinct=True),
    # Counting the number of comments related to the object, also ensuring distinct counting.
    comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')  # Ordering the results by the creation date of the main object, newest first.

    # Setting up filter backends to allow dynamic ordering of the queryset in the API.
    filter_backends = [
        filters.OrderingFilter,  # Using Django REST framework's OrderingFilter.
        filters.SearchFilter,   # Using Django REST framework's SearchFilter.
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    # Specifying the fields that can be used for ordering in API requests.
    ordering_fields = [
    'likes_count',          # Allowing ordering by the count of likes.
    'comments_count',       # Allowing ordering by the count of comments.
    'likes__created_at',    # Allowing ordering by the creation date of likes.
    ]

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
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')