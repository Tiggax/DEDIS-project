from django.contrib.auth.models import AbstractUser
from django.db import models
from django_summernote.fields import SummernoteTextField

class ClimbUser(AbstractUser):
    PERMISSIONS = (
        ("U","Unapproved"),
        ("A", "Approved"),
        ("M", "Moderator")
    )

    RANKS = (
        ("A", "Apprentice"),
        ("J", "Junior"),
        ("S", "Senior"),
        ("P", "Alpinist"),
        ("I", "Alpinist Instructor")
    )

    permission = models.CharField(max_length=1, choices=PERMISSIONS, default="U")
    rank = models.CharField(max_length=1, choices=RANKS, default="A")
    profile_pic = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.username


    