from api import settings
from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteWidget

from pages.models import Report, NewsPost

class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":"2", "cols":"44"}))

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["title", "content", "route"]
        widgets = {
            "content" : SummernoteWidget(),
        }

class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ["title", "content"]
        widgets = {
            "content" : SummernoteWidget(),
        }