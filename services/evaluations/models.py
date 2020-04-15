from django.db import models


class Evaluation(models.Model):
    """
    DESCRIPTION
    """
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='.')
    results = models.CharField(max_length=2000, null=True, blank=True)

    objects = models.Manager()

