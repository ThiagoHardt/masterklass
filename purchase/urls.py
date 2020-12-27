from django.urls import path, include
from . import views

urlpatterns = [
    path('plans/', views.plans, name='plans'),
]
