from django.db import models

# Create your models here.
class WebUser(models.Model):
    email = models.CharField(max_length=70, blank=False)