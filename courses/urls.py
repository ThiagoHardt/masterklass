from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.getCourses, name='courses'),
    path('<course_id>', views.courseDetail, name='course_detail'),
]
