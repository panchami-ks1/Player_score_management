from tabnanny import verbose
from django.db import models


# Create your models here.

class Players(models.Model):
    Name=models.CharField(max_length=255)
    Nationality=models.CharField(max_length=255)
    Overall=models.IntegerField()
    class Meta:
        verbose_name_plural='Players'


    def __str__(self):
       return self.Name
