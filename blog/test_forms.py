from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self): # defined a function
        comment_form = CommentForm({'body': 'This is a great post'}) # filled the form with string to make sure the comment form is valid
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid') # Finally, using an assert to determine if the form is valid. Since the body field is required, and we have provided some content, the test should pass.

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg='Form is valid')