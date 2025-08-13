from django.db import models



class  URL(models.Model):
    long_url =  models.CharField(blank=False)
    short_key = models.CharField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
