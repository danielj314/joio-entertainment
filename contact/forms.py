from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form to allow users to contact company """
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Name',
            'email': 'Email',
            'message': 'Message',
        }

        for field in self.fields:
            self.fields[field].label = labels[field]
