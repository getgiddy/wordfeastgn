from django.contrib.auth.models import User
from django import forms

from blog.models import AuthorProfile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = AuthorProfile
        fields = [
            'avatar',
            'bio',
            'website',
            'twitter',
            'facebook',
            'instagram',
        ]
