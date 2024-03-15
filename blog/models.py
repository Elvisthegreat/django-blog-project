from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) # character field with a max length of 200 characters.
    slug = models.SlugField(max_length=200, unique=True) # slug field a slug is a short name for an article that is still in production.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts" 
    ) # Foreign Key. One user can write many posts, so this is a one-to-many or Foreign Key
    content = models.TextField() # text field
    created_on = models.DateTimeField(auto_now_add=True) # created time is the time of post entry.
    status = models.IntegerField(choices=STATUS, default=0) # The option choices use the STATUS constant to limit the integer choice to 0 or 1 and has mapped these two integers to "Draft" and "Published".
    excerpt = models.TextField(blank=True) # As the excerpt is optional, the user must be able to leave this database row blank without throwing an error.
    updated_on = models.DateTimeField(auto_now=True) # The auto_now argument for the updated_on field sets the value to the current date and time whenever the record is saved, not just when it is created.
    