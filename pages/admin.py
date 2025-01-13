from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *

# Register your models here.

class SummerContentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Mountain)
admin.site.register(Route)
admin.site.register(Report, SummerContentAdmin)
admin.site.register(GalleryImage)
admin.site.register(Comment, SummerContentAdmin)
admin.site.register(Tag)
admin.site.register(NewsPost, SummerContentAdmin)