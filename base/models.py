from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


work_type_choices = (
    ('Office', 'office'),
    ('Hybrid', 'hybrid'),
    ('remote', 'Remote')
)


class Job(models.Model):
    content = models.TextField(default="")
    standard_advertisements = models.CharField(max_length=100)
    published = models.DateTimeField(default=timezone.now)
    deadline = models.DateField(auto_now_add=False, blank=True)
    provided_by = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=155, null=True, blank=True)
    work_type = models.CharField(choices=work_type_choices, max_length=10, default="Not specified")

    def __str__(self):
        return self.standard_advertisements

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})
