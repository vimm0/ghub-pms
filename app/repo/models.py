from django.db import models


class Repo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
