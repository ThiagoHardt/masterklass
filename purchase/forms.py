from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Username',
            'email': 'Email Address',
            'password': 'Password',
        }

        self.fields['username'].widget.attrs['autofocus'] = True
        self.fields["email"].required = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
