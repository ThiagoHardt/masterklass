from django import forms
from .models import Course, Category, Lesson, Comment


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


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ["body", ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["body"].label = "Comment"
        self.fields["body"].widget.attrs["rows"] = 3
