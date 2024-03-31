from . import views
from django.urls import path

"""check the name of your function then add for 
about_me, use it for the views."""

urlpatterns = [
    path('', views.about_me, name='about'),
]