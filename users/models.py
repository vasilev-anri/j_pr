from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    image = models.ImageField(upload_to='company_logos', default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
