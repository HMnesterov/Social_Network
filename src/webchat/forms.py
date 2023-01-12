from django import forms

from webchat.models import Chat


class CreateChatForm(forms.ModelForm):
    title = forms.CharField(max_length=150, label='New chat ')

    class Meta:
        model = Chat
        fields = ['title']
