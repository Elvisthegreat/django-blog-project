from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField # imported cloudinary

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`
    """
    title = models.CharField(max_length=200, unique=True) # character field with a max length of 200 characters.
    slug = models.SlugField(max_length=200, unique=True) # slug field a slug is a short name for an article that is still in production.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts" 
    ) # Foreign Key. One user can write many posts, so this is a one-to-many or Foreign Key
    featured_image = CloudinaryField('image', default='placeholder') # for CLOUDINARY
    content = models.TextField() # text field
    created_on = models.DateTimeField(auto_now_add=True) # created time is the time of post entry.
    status = models.IntegerField(choices=STATUS, default=0) # The option choices use the STATUS constant to limit the integer choice to 0 or 1 and has mapped these two integers to "Draft" and "Published".
    excerpt = models.TextField(blank=True) # As the excerpt is optional, the user must be able to leave this database row blank without throwing an error.
    updated_on = models.DateTimeField(auto_now=True) # The auto_now argument for the updated_on field sets the value to the current date and time whenever the record is saved, not just when it is created.


    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"The title of this post is {self.title} | written by {self.author}"


class Comment(models.Model):

    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField() # the comment body field section
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    class Mata:
        ordering= ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
    