from django.test import TestCase
from django.urls import reverse
from .forms import CollaborateForm
from .models import About

class AboutBlogView(TestCase):

    """ Testing views with GET """
    def setUp(self):
        """Creates about me content"""
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()

    

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about')) # The about point to the name of our urls.py
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)