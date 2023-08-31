from django.db import models
from django.urls import reverse

class Post(models.Model):
    """A class that allows user to post content."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        """Returns the string representation for the class."""
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
