from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
        # fields = '__all__'  # Include all fields from the model except the "read" field
        # exclude = ['read']  # Exclude the "read" field from the form