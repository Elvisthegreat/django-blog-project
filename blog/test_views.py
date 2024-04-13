from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

class TestBlogViews(TestCase):
    """The setUp method is a special method we can use in our tests to provide initial settings for our tests to use.
    In this case, we create a superuser and a small blog post in our test database. This data is then assigned as a variable
    of the self object. To run our post_detail view, we need an instance of Post to render. As an instance
    of Post requires a ForeignKey to a User for its author field, we first needed to create a superuser to 
    author the blog post: author=self.user"""

    def setUp(self):
        """ A small setup model for testing """
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content) # It checks whether the first argument (in this case, "Blog title") is present in the second argument (in this case, response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm) # Verifies that the comment_form from the post_detail view's context is an instance of the CommentForm class.