from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    time_Choices = (('230', '230'), ('330', '330'), ('430', '430'), ('530', '530'), ('630', '630'))
    level_Choices = (('A', 'A'), ('A+', 'A+'), ('B', 'B'), ('B+', 'B+'), ('C', 'C'), ('C+', 'C+'))
    mem_time = models.CharField(max_length=100, choices=time_Choices, blank=True, null=True)
    mem_level = models.CharField(max_length=100, choices=level_Choices, blank=True, null=True)
    total_points = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    level = models.CharField(max_length=100)
    def __str__(self):
        return self.level

