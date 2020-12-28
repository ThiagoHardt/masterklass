from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    slug = models.SlugField()
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.title

    @property
    def lessons(self):
        return self.lessons_set.all().order_by("position")


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=155)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.URLField(max_length=1024, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
