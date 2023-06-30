# notas/models.py
from django.contrib.auth.models import User
from django.db import models

class Notas(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):

        return F"{self.title}"
