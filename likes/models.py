# Importing the necessary Django modules to define a model
from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Definition of the Like model
class Like(models.Model):
    """
    Like model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    # owner field - a foreign key that references the User model. 
    # It represents the user who created the like. On deletion of the user, the like will be deleted as well.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # post field - a foreign key that references the Post model. 
    # It represents the post that is liked. The related_name 'likes' allows access to likes from the Post model.
    # On deletion of the post, the like will be deleted as well.
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )

    # created_at field - a DateTimeField that records the time when the like was created.
    # auto_now_add=True ensures that this field is automatically set to the current date and time when a Like is created.
    created_at = models.DateTimeField(auto_now_add=True)

    # Meta subclass to provide additional information about the Like model
    class Meta:
        ordering = ['-created_at']  # Default ordering of likes - newest first
        unique_together = ['owner', 'post']  # Ensures that a user can like a post only once

    # __str__ method to define the string representation of a Like object
    def __str__(self):
        # Returns a string that includes the username of the owner and the title of the post
        return f'{self.owner} {self.post}'
