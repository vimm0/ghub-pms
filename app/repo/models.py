from django.db import models
from django.core.validators import URLValidator

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

    def save(self):
        from git import Repo
        from github import Github

        # using username and password
        # g = Github("vimm0", "vim9815510732")

        # or using an access token
        g = Github(self.user.git_token)
        repo_name = g.get_user().get_repo(self.name)
        self.repo_full_name = repo_name.full_name
        self.owner_name = repo_name.owner.name
        self.owner_username = repo_name.owner.login
        self.language = repo_name.language
        self.last_modified = repo_name.last_modified
        self.size = repo_name.size
        self.clone_url = repo_name.clone_url
        self.issues_url = repo_name.issues_url
        self.merges_url = repo_name.merges_url
        self.milestones_url = repo_name.milestones_url
        self.comments_url = repo_name.comments_url
        self.commits_url = repo_name.commits_url
        import ipdb
        ipdb.set_trace()
        # for repo in g.get_user().get_repos():
        #     print(repo.name)
        #     repo.edit(has_wiki=False)

        pass
