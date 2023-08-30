from django.db import models

class Post(models.Model):
    """A class for our posts."""
    text = models.TextField()
