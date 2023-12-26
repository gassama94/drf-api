# Importing necessary Django and Django REST framework classes
from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

# ProfileList class for handling the listing of profiles
class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by Django signals.
    """
    # Annotating the queryset to include counts of posts, followers, and following for each profile.
    # Using 'distinct=True' to avoid duplicate counts in case of multiple related objects.
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')  # Ordering profiles by creation date, newest first.

    serializer_class = ProfileSerializer  # Specifying the serializer class for the Profile model.

    # Configuring filter backends to allow ordering of the results.
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__following__followed__profile',
    ]
    
    # Defining fields allowed to be used for ordering in the API requests.
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]

# ProfileDetail class for handling the retrieval and update of a specific profile
class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]  # Custom permission - allows operations only if the user is the owner of the profile.
    # Using the same annotated queryset as in ProfileList to include counts in the detailed view.
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class =  ProfileSerializer  # Specifying the serializer class for the Profile model.
