from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(unique=True, max_length=100)
    points = models.IntegerField(default=0)
    group = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name