# Importing necessary Django and Django REST framework modules
from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like

# LikeSerializer class definition
class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    # owner field - defined as a read-only field. 
    # This means it will be included in serialized representations, but won't be used for updating model instances.
    # The 'source' argument specifies that the field gets its value from the 'owner.username' attribute of the Like model.
    owner = serializers.ReadOnlyField(source='owner.username')

    # Meta subclass - contains metadata about the serializer
    class Meta:
        model = Like  # Specifies the model associated with this serializer
        fields = ['id', 'created_at', 'owner', 'post']  # Fields of the Like model to be included in the serialization

    # create method - overridden to handle unique constraint violations
    def create(self, validated_data):
        try:
            # Attempting to create a new Like instance. If successful, it returns the created Like instance.
            return super().create(validated_data)
        except IntegrityError:
            # Catching IntegrityError which occurs if the Like violates the unique constraint (same user liking the same post more than once)
            # Raising a ValidationError with a custom message indicating a possible duplicate like attempt
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
