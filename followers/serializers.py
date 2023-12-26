# Importing necessary modules from Django and Django REST framework
from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower

# Definition of the FollowerSerializer class
class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    Create method handles the unique constraint on 'owner' and 'followed'
    """
    # owner field - defined as a read-only field, it will not be used for creating or updating instances.
    # It gets its value from the 'username' attribute of the 'owner' field of the Follower model.
    owner = serializers.ReadOnlyField(source='owner.username')

    # followed_name field - also a read-only field.
    # It gets its value from the 'username' attribute of the 'followed' field of the Follower model.
    followed_name = serializers.ReadOnlyField(source='followed.username')

    # Meta subclass - contains metadata about the serializer
    class Meta:
        model = Follower  # Specifies the model associated with this serializer
        fields = [
            'id', 'owner', 'created_at', 'followed', 'followed_name'
        ]  # Fields of the Follower model to be included in the serialization

    # create method - overridden to handle unique constraint violations
    def create(self, validated_data):
        try:
            # Attempting to create a new Follower instance. If successful, it returns the created instance.
            return super().create(validated_data)
        except IntegrityError:
            # Catching IntegrityError, which occurs if the Follower violates the unique constraint 
            # (i.e., the same user trying to follow the same person more than once).
            # Raising a ValidationError with a custom message indicating a possible duplicate follow attempt.
            raise serializers.ValidationError({'detail': 'possible duplicate'})
