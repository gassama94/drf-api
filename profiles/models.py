from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Define your Profile model
class Profile(models.Model):
    # Additional fields for the profile

    # Link the profile to a user using a one-to-one relationship
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    # Timestamps for when the profile was created and last updated
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Profile-specific fields
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    
    # Field for storing an image (you might want to configure MEDIA_ROOT and MEDIA_URL in your settings)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_fvwztb_vlnjbh'
    )

    class Meta:
        # Define the default ordering for profiles based on creation date
        ordering = ['-created_at']

    def __str__(self):
        # Define how the profile should be represented as a string
        return f"{self.owner}'s profile"
    
# Define a function to create a profile when a new user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Create a profile associated with the newly created user
        Profile.objects.create(owner=instance)

# Connect the create_Profile function to the post_save signal of the User model
post_save.connect(create_profile, sender=User)
