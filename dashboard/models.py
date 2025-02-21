from django.db import models

from members.models import Level


# Create your models here.
class Dashboard(models.Model):

    level_Choices = (('A', 'A'), ('A+', 'A+'),
                   ('B', 'B'), ('B+', 'B+'),
                   ('C', 'C'), ('C+', 'C+'),
    )

    first_class = models.CharField(max_length=100, choices=level_Choices)
    second_class = models.CharField(max_length=100, choices=level_Choices)
    third_class = models.CharField(max_length=100, choices=level_Choices)
    fourth_class = models.CharField(max_length=100, choices=level_Choices)
    fifth_class = models.CharField(max_length=100, choices=level_Choices)


    def __str__(self):
        return 'class'