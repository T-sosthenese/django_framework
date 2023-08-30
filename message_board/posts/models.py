from django.db import models

class Post(models.Model):
    """A class for our posts."""
    text = models.TextField()

    def __str__(self):
        """Returns a string representation of the post."""
        return self.text[:50] + '...'
