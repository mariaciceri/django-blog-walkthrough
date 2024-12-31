from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateRequestForm

def about_detail(request):
    """
    Display an individual :model:`about.About`.

    **Context**

    ``about``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about.html`
    """

    if request.method == "POST":
        collab_requests = CollaborateRequestForm(data=request.POST)
        if collab_requests.is_valid():
            collab_requests.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days."
            )

    collab_requests = CollaborateRequestForm()
    about = About.objects.all().order_by("-created_on").first()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collab_requests": collab_requests, 
        },
    )