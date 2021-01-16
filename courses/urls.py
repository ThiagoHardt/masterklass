from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.getCourses, name='courses'),
    path('<course_id>', views.courseDetail, name='course_detail'),
    path('manage_category/', views.manageCategory, name='manage_category'),
    path('manage_course/', views.manageCourse, name='manage_course'),
    path('add_course/', views.addCourse, name='add_course'),
    path('update_course/<id>', views.updateCourse, name='update_course'),
]
