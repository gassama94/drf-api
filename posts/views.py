from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer

class PostList(APIView):
    # Specifies the serializer class used for Post data
    serializer_class = PostSerializer

    # Sets the permission classes - authenticated users or read-only access for unauthenticated users
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        # Handles GET requests, retrieves all Post instances
        posts = Post.objects.all()

        # Serializes the Post data, including context for handling request-based fields
        serializer = PostSerializer(
            posts, many=True, context={'request': request}
        )

        # Returns the serialized Post data with an HTTP 200 status
        return Response(serializer.data)

    def post(self, request):
        # Handles POST requests, creating a new Post instance from the request data
        serializer = PostSerializer(
            data=request.data, context={'request': request}
        )

        # Validates the serializer and saves if valid, assigning the current user as the owner
        if serializer.is_valid():
            serializer.save(owner=request.user)
            # Returns the newly created Post data with an HTTP 201 status
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        
        # Returns any validation errors with an HTTP 400 status
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
