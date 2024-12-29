from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Mountain)
admin.site.register(Route)
admin.site.register(Report)
admin.site.register(GalleryImage)
admin.site.register(Comment)
admin.site.register(PostTag)
admin.site.register(NewsPost)