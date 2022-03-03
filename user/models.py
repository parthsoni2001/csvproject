from django.db import models
from django.db.models.base import Model

# Create your models here.
class UploadCSV(models.Model):
    upload = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return str(self.upload)