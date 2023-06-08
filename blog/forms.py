from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form to add a comment from the user.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            "body": "Share your plant experience here.",
        }


class EditForm(forms.ModelForm):
    """
    Form to edit a comment from the user.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            "body": "Make your changes below and click save",
        }
