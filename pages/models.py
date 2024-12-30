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

class Report(models.Model):
    title = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    report_creator = models.ForeignKey(
        ClimbUser, 
        on_delete = models.CASCADE,
        related_name="report_creator"
    )
    route = models.ForeignKey(Route, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.title}-{self.created}"

class GalleryImage(models.Model):
    def gallery_path(instance, filename):
        return f"gallery/{instance.created.year}/{instance.created.month}/id_{instance.gallery.id}/{filename}"
    image = models.FileField(upload_to = gallery_path)
    created = models.DateField(auto_now_add = True)
    gallery = models.ForeignKey(Report, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.image.name}"

class Comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    comment_creator = models.ForeignKey(
        ClimbUser, 
        on_delete = models.CASCADE,
        related_name="comment_creator"
    )
    report_id = models.ForeignKey(Report, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.comment_creator.username}: {self.created}"

class PostTag(models.Model):
    tag = models.CharField( max_length = 20)
    def __str__(self):
        return f"#{self.tag}"

class NewsPost(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    title = models.TextField()
    content = models.TextField()
    post_author = models.ForeignKey(
        ClimbUser,
        on_delete = models.CASCADE,
        related_name="post_author"
    )
    tags = models.ManyToManyField(PostTag)
    
    def __str__(self):
        return f"{self.title}"
