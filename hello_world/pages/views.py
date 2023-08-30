from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """A homepage class that inherits from django's TemplateView class."""
    template_name = "home.html"
