from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Categories are defined by this model.

    fields: slug and name
    required: slug and name
    """

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    slug = models.SlugField()
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    Courses are defined by this model.

    fields: category, title, description and thumbnail
    required: category and  title 
    """
    category = models.ForeignKey(
        "Category", null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=1024, blank=True, null=True)
    thumbnail = models.ImageField(
        default="default-image.png", upload_to='media')

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """
    Lessons are defined by this model.

    fields: slug, title, course, position, video_url and add_on
    required: slug, title, course, position, video_url 
    """
    class Meta:
        ordering = ("-add_on",)

    slug = models.SlugField()
    title = models.CharField(max_length=155)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    position = models.IntegerField()
    video_url = models.URLField(max_length=1024, null=True)
    add_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Comments are defined by this model.

    fields: course, author, body, and created_on
    required: course, author, body  
    """
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='comments', default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment by {}'.format(self.author)
