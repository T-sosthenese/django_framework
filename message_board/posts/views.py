from django.views.generic import ListView

from .models import Post

class HomePageView(ListView):
    """Custom view our homepage content."""
    model = Post
    template_name = "home.html"
