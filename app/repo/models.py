from datetime import datetime

from django.db import models
from django.core.validators import URLValidator


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Categories"


class Repo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    repo_full_name = models.CharField(max_length=255, null=True, blank=True)
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    owner_username = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    git_last_modified = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True, default=datetime.now)
    size = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    clone_url = models.TextField(validators=[URLValidator()], null=True, blank=True, help_text='Do not edit.')
    issues_url = models.TextField(validators=[URLValidator()], null=True, blank=True, help_text='Do not edit.')
    merges_url = models.TextField(validators=[URLValidator()], null=True, blank=True, help_text='Do not edit.')
    milestones_url = models.TextField(validators=[URLValidator()], null=True, blank=True, help_text='Do not edit.')
    comments_url = models.TextField(validators=[URLValidator()], null=True, blank=True, help_text='Do not edit.')
    commits_url = models.TextField(validators=[URLValidator()], null=True, blank=True, help_text='Do not edit.')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
