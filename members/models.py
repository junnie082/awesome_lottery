from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(unique=True, max_length=100)
    group_time_mode = models.CharField(max_length=100)
    group_level_mode = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    level = models.CharField(unique=True, max_length=100)
    def __str__(self):
        return self.level

