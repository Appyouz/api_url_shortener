from django.db import models


class  URL(models.Model):
    long_url =  models.CharField(max_length=2000, unique=True)
    short_key = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.short_key} -> {self.long_url}'
