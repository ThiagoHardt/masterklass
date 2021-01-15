from django import forms
from .models import Course, Category, Lesson


class UpdateCourseForm(forms.ModelForm):
    class Meta():
        model = Course
        fields = ["category", "title", "description", "thumbnail"]


class UpdateCategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = ["slug", "name"]


class UpdateLessonForm(forms.ModelForm):
    class Meta():
        model = Lesson
        fields = ["id", "slug", "title", "course", "position", "video_url"]
