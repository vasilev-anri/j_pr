from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
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


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['standard_advertisements', 'content', 'deadline']

    def form_valid(self, form):
        form.instance.provided_by = self.request.user
        return super().form_valid(form)










def contact(request):
    return render(request, 'base/contact.html')


def about(request):
    return render(request, 'base/about.html')

