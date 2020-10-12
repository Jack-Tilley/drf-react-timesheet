from django.db import models

# Create your models here.
class TimeSheet(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField(auto_now_add=True, editable=True)
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title