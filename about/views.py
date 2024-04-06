from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """ Display the latest 'About' content """

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
        "about": about,
        "collaborate_form": collaborate_form,
        }
    )
