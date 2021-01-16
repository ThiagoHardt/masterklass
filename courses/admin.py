from django.contrib import admin
from .models import Course, Lesson, Category, Comment


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


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)


admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment, CommentAdmin)
