from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Auth(models.Model):
    name = models.CharField(max_length=256)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name