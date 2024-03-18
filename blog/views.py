from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) # we can use .filter(author=1) or 2 or 3 to get a certain post and author
    template_name = "post_list.html" # If we did want a different template name, then we can set it using template_name =  like we did in our example.

