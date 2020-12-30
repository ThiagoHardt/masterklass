from django.contrib import admin
from .models import Course, Lesson, Category


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category"
    )


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "course"
    )

    ordering = ("course",)


admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
