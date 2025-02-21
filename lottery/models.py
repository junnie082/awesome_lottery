from django.db import models

from members.models import Member

# Create your models here.
class Point(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    points = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member.name