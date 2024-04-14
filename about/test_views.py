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


    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            'name': 'Elvis blessing',
            'email': 'elvis@gmail.com',
            'message': 'Lets collaborate'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request received! I endeavor to respond within 2 working days.",
            response.content
        
        )