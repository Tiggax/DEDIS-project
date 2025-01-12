from api import settings
from django import forms

from django_summernote.fields import SummernoteTextFormField


class CommentForm(forms.Form):
    content = SummernoteTextFormField()