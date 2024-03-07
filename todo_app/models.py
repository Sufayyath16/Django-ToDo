from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    date=models.CharField(max_length=255)
    status=models.CharField(max_length=255)


