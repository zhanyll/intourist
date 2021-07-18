from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    decription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0)
    is_publicated = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'Места'
        ordering = ['name']

