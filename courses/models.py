from django.db import models


class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=155)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
