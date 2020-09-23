from django.db import models
# Create your models here.


class ImageSet(models.Model):
    pdf_file = models.FileField(upload_to='')
