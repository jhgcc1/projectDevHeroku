
from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="build/static",
        max_length=254, blank=True, null=True
    )