from django.db import models

# Create your models here.
class Mijoz(models.Model):
    ism = models.CharField(max_length=25)
    raqam = models.IntegerField(default=0)
    yosh = models.IntegerField(default=0)
    address = models.TextField(blank=True,null=True)
    raqam2 = models.IntegerField(default=0)
    dokon_nomi = models.CharField(max_length=25)
    