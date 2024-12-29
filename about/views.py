from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About

def about_detail(request):
    """
    Display an individual :model:`about.About`.

    **Context**

    ``about``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about.html`
    """

    about = About.objects.all().order_by("-created_on").first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )