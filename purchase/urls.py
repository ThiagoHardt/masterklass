from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.plans, name='plans'),
    path('purchase/<int:plan_id>/', views.purchasePlan, name='purchase_plan'),
    path('signup/', views.signup, name='signup'),
    path('pre_validade_user/',
         views.preValidadeUser, name='pre_validade_user'),
]
