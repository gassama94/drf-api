from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly

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
    
class PostDetail(APIView):
    # Sets permission classes and serializer class for the view
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer

    def get_object(self, pk):
        try:
            # Tries to retrieve a post by its primary key (pk)
            post = Post.objects.get(pk=pk)
            # Checks if the request user has the right permissions for the post
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            # Raises an Http404 error if the post does not exist
            raise Http404

    def get(self, request, pk):
        # Handles GET requests for a single post
        post = self.get_object(pk)
        # Serializes the post data
        serializer = PostSerializer(post, context={'request': request})
        # Returns the serialized data
        return Response(serializer.data)

    def put(self, request, pk):
        # Handles PUT requests for updating a single post
        post = self.get_object(pk)
        # Serializes the post with the data from the request
        serializer = PostSerializer(post, data=request.data, context={'request': request})
        if serializer.is_valid():
            # Saves the post if the data is valid
            serializer.save()
            # Returns the updated post data
            return Response(serializer.data)
        # Returns validation errors if the data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Handles DELETE requests for a single post
        post = self.get_object(pk)
        # Deletes the post
        post.delete()
        # Returns an HTTP 204 No Content status to indicate successful deletion
        return Response(status=status.HTTP_204_NO_CONTENT)
