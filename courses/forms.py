from django import forms
from .models import Course, Category, Lesson


class CourseForm(forms.ModelForm):
    class Meta():
        model = Course
        fields = ["title", "category", "description", "thumbnail"]


class UpdateCategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = ["slug", "name"]


class LessonForm(forms.ModelForm):
    class Meta():
        model = Lesson
        fields = ["slug", "title", "course", "position", "video_url"]
