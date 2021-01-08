from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Course, Lesson, Category


def getCourses(request):
    """A view to return a list of all courses."""
    currentCategory = Category.objects.all()
    categories = Category.objects.all()
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    query = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "Please enter a search criteria")
                return redirect(reverse("courses"))

            queries = Q(title__icontains=query) | Q(
                description__icontains=query) | Q(category__slug__icontains=query)
            categoryQ = Q(slug__icontains=query)
            courses = courses.filter(queries)
            currentCategory = categories.filter(categoryQ)

    context = {
        "courses": courses,
        "categories": categories,
        "lessons": lessons,
        "currentCategory": currentCategory,
        "searchTerm": query,
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
