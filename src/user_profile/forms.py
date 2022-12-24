from django import forms

from user_profile.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']