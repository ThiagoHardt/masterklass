from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.plans, name='plans'),
    path('purchase/', views.purchasePlan, name='purchase_plan'),
    path('signup/', views.signup, name='signup'),
]
