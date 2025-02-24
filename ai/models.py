from django.db import models

# Create your models here.
class SpeakingBook(models.Model):
    dailyProgress = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)