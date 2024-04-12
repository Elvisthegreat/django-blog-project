from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Elvis',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_is_valid_one(self):
        """check that the form is not valid if we fail 
        to populate one of the fields in the dictionary."""

        form_one = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hey!'
        })
        self.assertFalse(form_one.is_valid(), msg="Form is not correctly populated")

    def test_form_is_valid_two(self):
        """check that the form is not valid if we fail 
        to populate one of the fields in the dictionary."""

        form_two = CollaborateForm({
            'name': 'Blessing',
            'email': 'test@amadin.com',
            'message': ''
        })
        self.assertFalse(form_two.is_valid(), msg='Form is not correctly populated')

    def test_form_is_valid_three(self):
        """check that the form is not valid if we fail 
        to populate one of the fields in the dictionary."""

        form_three = CollaborateForm({
            'name': 'Amadin',
            'email': '',
            'message': 'Ho!'
        })
        self.assertFalse(form_three.is_valid(), msg='Form is not correctly populated')