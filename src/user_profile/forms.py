from django import forms

from user.models import Person
from user_profile.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']


class UserProfileEdit(forms.Form):
    photo = forms.ImageField(label="Profile image", initial='photo')
    bio = forms.CharField(required=False, max_length=200, label="BIO", initial='bio')
    status = forms.CharField(required=False, max_length=20, label="Status", initial='status')

