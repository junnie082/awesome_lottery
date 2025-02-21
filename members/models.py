from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(unique=True, max_length=100)
    time_Choices = (('230', '230'), ('330', '330'), ('430', '430'), ('530', '530'), ('630', '630'))
    level_Choices = (('A', 'A'), ('A+', 'A+'), ('B', 'B'), ('B+', 'B+'), ('C', 'C'), ('C+', 'C+'))
    group_time_mode = models.CharField(max_length=100, choices=time_Choices)
    group_level_mode = models.CharField(max_length=100, choices=level_Choices)
    total_points = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    level = models.CharField(unique=True, max_length=100)
    def __str__(self):
        return self.level

