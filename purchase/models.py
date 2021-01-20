from django.db import models

PLAN_CHOICES = (
    ('lifetime', 'Life Time'),
    ('yearly', 'Yearly'),
    ('monthly', 'Monthly')
)


class Plan(models.Model):
    """
    Plans are defined by this model.

    fields: slug, name, description, price, active
    required: slug, name, description, price 
    """
    slug = models.SlugField(choices=PLAN_CHOICES, default='lifetime')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name
