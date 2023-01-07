from django import forms

from webchat.models import Chat


class CreateChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['title']