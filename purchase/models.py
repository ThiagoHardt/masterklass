from django.db import models

PLAN_CHOICES = (
    ('lifetime', 'Life Time'),
    ('yearly', 'Yearly'),
    ('monthly', 'Monthly')
)


class Plan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(choices=PLAN_CHOICES, default='lifetime')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
