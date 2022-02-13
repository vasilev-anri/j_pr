from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .models import Job


class JobListView(ListView):
    model = Job
    template_name = 'base/home.html'
    context_object_name = 'jobs'
    ordering = ['-published']


class UserJobListView(ListView):
    model = Job
    template_name = 'base/user_job.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Job.objects.filter(provided_by=user).order_by('-published')


class JobDetailView(DetailView):
    model = Job


def contact(request):
    return render(request, 'base/contact.html')


def about(request):
    return render(request, 'base/about.html')

