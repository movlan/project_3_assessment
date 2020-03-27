from django.db import models
from django.urls import reverse


class Wish(models.Model):
    text = models.TextField(max_length=200)
    
    def get_absolute_url(self):
        return reverse('index')
