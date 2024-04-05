from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) # we can use .filter(author=1) or 2 or 3 to get a certain post and author
    template_name = "blog/index.html"
    paginate_by = 6 # this tells to display 6 blog post at a time on the homepage, we change to any number

# function for our post_detail to dsiplay a single blog post
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid(): # means that the form has been filled out correctly
            comment = comment_form.save(commit=False) # Save, but not to the database not until a user click save button 
            comment.author = request.user
            comment.post = post # We also set the post field using the post variable, which contains the result of the get_object_or_404
            comment.save() # call the save method to write the data to the database when the save button i click
            # for success message
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
    )
    
    comment_form = CommentForm() # Reset to blank after comment is submitted
    print( "About to render template")

    return render(
        request,
        "blog/post_detail.html",
        # Context key and value pairs as a dictionary
        {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )
