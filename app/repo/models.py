from datetime import datetime

from django.db import models
from django.core.validators import URLValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.user.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"


class Repo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    repo_full_name = models.CharField(max_length=255, null=True, blank=True)
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    owner_username = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
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


@receiver(post_save, sender=Repo, dispatch_uid="update_repo_meta_count")
def repo_meta(sender, instance, **kwargs):
    # from git import Repo
    from github import Github

    # using username and password
    # g = Github("vimm0", "vim9815510732")
    if instance.repo_full_name is None:
        # or using an access token
        g = Github(instance.user.git_token)
        repo_name = g.get_user().get_repo(instance.name)
        obj = Repo.objects.get(pk=instance.id)

        obj.repo_full_name = repo_name.full_name
        obj.owner_name = repo_name.owner.name
        obj.owner_username = repo_name.owner.login
        obj.language = repo_name.language
        obj.last_modified = datetime.strptime(repo_name.last_modified, '%a, %d %b %Y %H:%M:%S %Z')
        obj.size = repo_name.size
        obj.clone_url = repo_name.clone_url
        obj.issues_url = repo_name.issues_url
        obj.merges_url = repo_name.merges_url
        obj.milestones_url = repo_name.milestones_url
        obj.comments_url = repo_name.comments_url
        obj.commits_url = repo_name.commits_url
        obj.save()
        # import ipdb
        # ipdb.set_trace()
        # User Token: c435e9c77b942e0220b313404667b2b1b4fcc8b5
    # super(Repo, self).save(*args, **kwargs)
