from django.shortcuts import render, get_object_or_404
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


def courseDetail(request, course_id):
    """ A view to show all lessons within a course """

    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('position')

    context = {
        'course': course,
        'lessons': lessons,
    }

    return render(request, 'courses/course_detail.html', context)
