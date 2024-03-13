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
    status = models.IntegerField(choices=STATUS, default=0)
