from django.db import models

# Create your models here.

class MyModel(models.Model):

    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ssd = models.CharField(max_length=100)
    hdd = models.CharField(max_length=100)
    gc = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    sn = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

