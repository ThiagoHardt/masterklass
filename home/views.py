from django.shortcuts import render
from courses.models import Lesson


def index(request):
    ''' Returns the index page with the last 3 lessons add in the system '''

    lessons = Lesson.objects.order_by('-add_on')[0:3]

    context = {
        "lessons": lessons,
    }

    return render(request, "home/index.html", context)
