from django.urls import path
from . views import JobListView, JobDetailView, UserJobListView
from . import views

urlpatterns = [
    path('', JobListView.as_view(), name='base-home'),
    path('user/<str:username>', UserJobListView.as_view(), name='user-jobs'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('contact/', views.contact, name='base-contact'),
    path('about/', views.about, name='base-about'),
]