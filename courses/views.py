from django.shortcuts import render
from .models import Course, Lesson, Category


def getCourses(request):
    """A view to return a list of all courses."""

    categories = Category.objects.all()
    courses = Course.objects.all()
    lessons = Lesson.objects.all()

    context = {
        "courses": courses,
        "categories": categories,
        "lessons": lessons,
    }

    return render(request, "courses/courses.html", context)
