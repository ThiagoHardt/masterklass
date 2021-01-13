from django.urls import path
from . import views

urlpatterns = [
    path('<user_id>', views.getUserProfile, name='getUserProfile'),
]
