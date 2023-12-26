from rest_framework import serializers
from posts.models import Post
from likes.models import Like

class PostSerializer(serializers.ModelSerializer):
    # Serializer fields to represent the 'owner' by their username
    owner = serializers.ReadOnlyField(source='owner.username')

    # SerializerMethodField to check if the current user is the owner of the post
    is_owner = serializers.SerializerMethodField()

    # Additional fields to represent the owner's profile ID and profile image URL
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()


    def validate_image(self, value):
        # Custom validation for the image field
        # Check if the image size exceeds 2MB
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')

        # Check if the image height exceeds 4096 pixels
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')

        # Check if the image width exceeds 4096 pixels
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')

        return value

    def get_is_owner(self, obj):
        # Method to determine if the request user is the owner of the post
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        # Meta class to specify the model and fields used in the serializer
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter', 
            'like_id',  'likes_count', 'comments_count',
        ]
