# Importing necessary classes from Django REST framework
from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

# ProfileList class for handling the listing of profiles
class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.all()  # The queryset representing the database query to be executed for profiles
    serializer_class = ProfileSerializer  # Specifies the serializer to use for formatting the response data

# ProfileDetail class for handling the retrieval and update of a specific profile
class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    This view handles GET requests for retrieving a profile and PUT/PATCH requests for updating a profile.
    """
    permission_classes = [IsOwnerOrReadOnly]  # Custom permission - allows operations only if the user is the owner of the profile
    queryset = Profile.objects.all()  # The queryset for retrieving the profile from the database
    serializer_class = ProfileSerializer  # Specifies the serializer for profile data
