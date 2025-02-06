from django.db import models

class URLMapping(models.Model):
    short_code = models.CharField(max_length=6, unique=True)
    long_url = models.URLField(unique=True)