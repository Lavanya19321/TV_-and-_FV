from django.db import models

# Create your models here.
class school(models.Model):
    sname=models.CharField(max_length=23)
    sprincipal=models.CharField(max_length=23)
    def __str__(self):
        return self.sname

