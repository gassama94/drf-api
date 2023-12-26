from django.db import models
from django.contrib.auth.models import User


class Categories(models.TextChoices):
    WORLD = 'world'
    ENVIRONMENT = 'environment'
    TECHNOLOGY = 'technology'
    DESIGN = 'design'
    CULTURE = 'culture'
    BUSINESS = 'business'
    POLITICS = 'politics'
    OPINION = 'opinion'
    SCIENCE = 'science'
    HEALTH = 'health'
    STYLE = 'style'
    TRAVEL = 'travel'



class Post(models.Model):
    """
    Defines the Post model, representing a post created by a user. Each post
    can have an associated image, a title, and content. The model also includes
    functionality for applying filters to images.
    """

    # Choices for image filters, each represented by a tuple of (code, readable name)
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'), 
        ('xpro2', 'X-pro II')
]
  
    # A foreign key to the User model, establishing a many-to-one relationship.
    # When a User is deleted, their posts are also deleted.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Auto-generated fields for tracking the creation and last update time of a post
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # The title of the post, limited to 255 characters
    title = models.CharField(max_length=255)

    # The main content of the post, can be left blank
    content = models.TextField(blank=True)

    # A choice field to categorize the post
    category = models.CharField(max_length=50, choices=Categories.choices,
                                default=Categories.WORLD)

    # An image associated with the post, stored in the 'images/' directory
    # Defaults to a specified image if none is provided
    image = models.ImageField(
        upload_to='images/', default='../default_post_i8rbz', blank=True
    )

    # Field for selecting an image filter, with a default value
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )


    class Meta:
        # Orders posts in descending order based on their creation time
        ordering = ['-created_at']

    def __str__(self):
        # String representation of a post, showing its ID and title
        return f'{self.id} {self.title}'


