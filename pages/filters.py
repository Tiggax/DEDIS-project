import django_filters
from .models import *

class NewsPostFilter(django_filters.FilterSet):

    class Meta:
        model = NewsPost
        fields = ['created', 'title', 'content', 'tags']


class ReportFilter(django_filters.FilterSet):
    
    class Meta:
        model = Report
        fields = ['title', 'created', 'content', 'creator', 'route']