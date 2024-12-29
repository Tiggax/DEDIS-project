from django.contrib.auth.models import AbstractUser
from django.db import models
from django_summernote.fields import SummernoteTextField

class ClimbUser(AbstractUser):
    pass
    def __str__(self):
        return self.username

class Invite(models.Model):
    created = models.DateTimeField(auto_created=True)
    accepted = models.DateTimeField()
    invite_creator = models.ForeignKey(
        ClimbUser, 
        on_delete=models.CASCADE,
        related_name="invite_creator"
    )
    invite_acceptor = models.ForeignKey(
        ClimbUser, 
        on_delete=models.CASCADE,
        related_name="invite_acceptor"
    )




    