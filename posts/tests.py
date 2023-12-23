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


class PostDetailViewTests(APITestCase):
    def setUp(self):
        # Sets up the initial data before each test method.
        # Two users, Adam and Brian, are created, each with their own post.
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Post.objects.create(owner=adam, title='a title', content='adams content')
        Post.objects.create(owner=brian, title='another title', content='brians content')

    def test_can_retrieve_post_using_valid_id(self):
        # Tests if a post can be retrieved using a valid ID.
        response = self.client.get('/posts/1/')
        # Asserts that the post with ID 1 has the correct title and that the response status is 200 OK.
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        # Tests if the system correctly handles attempts to retrieve a post using an invalid ID.
        response = self.client.get('/posts/999/')
        # Asserts that the response status is 404 Not Found for a non-existent post ID.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        # Tests if a user can update their own post.
        # Logs in as user 'adam'.
        self.client.login(username='adam', password='pass')
        # Attempts to update the post with ID 1, which belongs to 'adam'.
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        # Asserts that the post's title is updated and the response status is 200 OK.
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        # Tests if a user is prevented from updating another user's post.
        # Logs in as user 'adam'.
        self.client.login(username='adam', password='pass')
        # Attempts to update the post with ID 2, which belongs to 'brian'.
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        # Asserts that the response status is 403 Forbidden, indicating 'adam' can't update 'brian's post.
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

