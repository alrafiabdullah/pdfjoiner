from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_paid = models.BooleanField(default=False)


class FileSet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='', unique=False)
    created_at = models.DateTimeField(auto_now=True)
