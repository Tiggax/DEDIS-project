from django.contrib.auth.models import AbstractUser
from django.db import models
from django_summernote.fields import SummernoteTextField

class ClimbUser(AbstractUser):
    pass
    def __str__(self):
        return self.username


    