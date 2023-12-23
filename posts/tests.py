from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

class PostListViewTests(APITestCase):
    def setUp(self):
        # This method sets up the necessary data before each test method is run.
        # Here, it's creating a user 'adam' with a password 'pass'.
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_posts(self):
        # Tests if posts can be listed correctly.
        # First, a user 'adam' is retrieved and a new post is created for him.
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='a title')

        # The test client makes a GET request to the '/posts/' endpoint.
        response = self.client.get('/posts/')

        # Checks if the response status code is 200 OK, indicating success.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Prints the response data and the number of items in the response for debugging.
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        # Tests if a logged-in user can create a post.
        # The test client logs in as the user 'adam'.
        self.client.login(username='adam', password='pass')

        # Makes a POST request to create a new post.
        response = self.client.post('/posts/', {'title': 'a title'})

        # Counts the number of posts to check if the post was created.
        count = Post.objects.count()
        # Asserts that one post was created and the response status is 201 CREATED.
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        # Tests that a user who is not logged in cannot create a post.
        # Makes a POST request without logging in.
        response = self.client.post('/posts/', {'title': 'a title'})

        # Asserts that the response status code is 403 FORBIDDEN.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
