import django_filters
from .models import *

class NewsPostFilter(django_filters.FilterSet):

    class Meta:
        model = NewsPost
        fields = ['created', 'title', 'content', 'author', 'tags']