from api import settings
from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteWidget


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
