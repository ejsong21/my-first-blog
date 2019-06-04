from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=150)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.title
# Create your models here.
