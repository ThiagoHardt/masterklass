from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Course, Lesson, Category
from .forms import UpdateCourseForm, UpdateCategoryForm, UpdateLessonForm
from django.contrib.auth.decorators import login_required


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


@login_required
def courseDetail(request, course_id):
    """ A view to show all lessons within a course """

    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('position')

    context = {
        'course': course,
        'lessons': lessons,
    }

    return render(request, 'courses/course_detail.html', context)


def manageCategory(request):
    """ A view to add categories """

    categories = Category.objects.all()
    categoryForm = UpdateCategoryForm()

    if request.method == "POST":
        if request.POST.__contains__("addBtn"):

            categoryForm = UpdateCategoryForm(request.POST)

            if categoryForm.is_valid():
                categoryForm.save()

                message = "Category added successfully."
                messages.success(request, message)

                return redirect("manage_category")

        elif request.POST.__contains__("updateBtn"):

            category = categories.filter(
                id=request.POST.get('categoryId')).first()
            categoryForm = UpdateCategoryForm(request.POST, instance=category)

            if categoryForm.is_valid():
                categoryForm.save()

                message = "Category updated successfully."
                messages.success(request, message)

                return redirect("manage_category")

        elif request.POST.__contains__("deleteBtn"):

            category = categories.filter(
                id=request.POST.get('categoryId')).delete()

            message = "Category deleted successfully."
            messages.success(request, message)

            return redirect("manage_category")
    else:
        categoryForm = UpdateCategoryForm()

    context = {
        "categories": categories,
        "categoryForm": categoryForm,
    }

    return render(request, "courses/manage_category.html", context)


def addCourse(request):
    """ A view to add courses, categories and lessons """

    categories = Category.objects.all()
    courses = Course.objects.all()
    lessons = Lesson.objects.all()

    courseForm = UpdateCourseForm()
    categoryForm = UpdateCategoryForm()
    lessonForm = UpdateLessonForm()

    context = {
        "courses": courses,
        "categories": categories,
        "lessons": lessons,
        "courseForm": courseForm,
        "categoryForm": categoryForm,
        "lessonForm": lessonForm,
    }

    return render(request, "courses/add_course.html", context)


def addLesson(request):
    """ A view to add courses, categories and lessons """

    categories = Category.objects.all()
    courses = Course.objects.all()
    lessons = Lesson.objects.all()

    courseForm = UpdateCourseForm()
    categoryForm = UpdateCategoryForm()
    lessonForm = UpdateLessonForm()

    context = {
        "courses": courses,
        "categories": categories,
        "lessons": lessons,
        "courseForm": courseForm,
        "categoryForm": categoryForm,
        "lessonForm": lessonForm,
    }

    return render(request, "courses/add_lesson.html", context)
