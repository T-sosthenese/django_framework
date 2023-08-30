from django.http import HttpResponse

def homePageView(request):
    """ A function that returns Hello World."""
    return HttpResponse("Hello, World!")
