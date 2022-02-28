from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=155, null=True, blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    content = models.TextField(default="info")
    standard_advertisements = models.CharField(max_length=100)
    published = models.DateTimeField(default=timezone.now)
    deadline = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    provided_by = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    # image = models.ImageField(upload_to='company_logos')
    description = models.TextField(default="")

    def __str__(self):
        return self.standard_advertisements
