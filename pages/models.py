import uuid

from django.db import models

from django_summernote.fields import SummernoteTextField

from api.models import ClimbUser

# Create your models here.


class Mountain(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name}"

class Route(models.Model):
    mountain = models.ForeignKey(
        Mountain, 
        on_delete = models.CASCADE,
        blank = True,
        null = True
    )
    name = models.TextField()
    def __str__(self):
        return f"{self.mountain} - {self.name}"

class Tag(models.Model):
    tag = models.CharField( max_length = 20)
    def __str__(self):
        return f"#{self.tag}"

class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    creator = models.ForeignKey(
        ClimbUser, 
        on_delete = models.CASCADE,
        related_name="reports"
    )
    route = models.ForeignKey(Route, on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name="report_tags")

    def __str__(self):
        return f"{self.title}-{self.created}"

class GalleryImage(models.Model):
    def gallery_path(instance, filename):
        return f"gallery/{instance.created.year}/{instance.created.month}/{instance.gallery.id}/{filename}"
    image = models.FileField(upload_to = gallery_path)
    created = models.DateField(auto_now_add = True)
    gallery = models.ForeignKey(Report, on_delete = models.CASCADE, related_name="gallery")

    def __str__(self):
        return f"{self.image.name}"

class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(
        ClimbUser, 
        on_delete = models.CASCADE,
        related_name="comments"
    )
    report_id = models.ForeignKey(Report, on_delete = models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.creator.username}: {self.created}"

class NewsPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add = True)
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(
        ClimbUser,
        on_delete = models.CASCADE,
        related_name="posts"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="post_tags")
    
    def __str__(self):
        return f"{self.title}"
