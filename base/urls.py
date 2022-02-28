from django.urls import path
from . views import JobListView, JobDetailView, UserJobListView, JobCreateView, JobUpdateView, JobDeleteView
from . import views

urlpatterns = [
    path('', JobListView.as_view(), name='base-home'),
    path('user/<str:username>', UserJobListView.as_view(), name='user-jobs'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('job/new/', JobCreateView.as_view(), name='job-create'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path('contact/', views.contact, name='base-contact'),
    path('about/', views.about, name='base-about'),
]