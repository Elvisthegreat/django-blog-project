from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post) # When we use a class, we register it with a decorator that is more Pythonic. Deleted the former post register below
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on') # These are the header names for the table of posts. title, slug, status. The created on display date
    search_fields = ['title', 'content'] # for our search option for post
    list_filter = ('status', 'created_on',) # to filter posts by their draft or published status.
    prepopulated_fields = {'slug': ('title',)} # This prepopulate the slug automatically when typing on the title field
    summernote_fields = ('content',) # This attribute inherits from the SummernoteModelAdmin class. to have all those we call easily use in the content like click on B header becomes bold

# Register your models here.
admin.site.register(Comment)
