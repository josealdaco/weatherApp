from django.db import models


# Create your models here.
class Comments(models.Model):
    """ This model Profile will be used to create A profile of the User"""
    comment = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=100, blank=True)
