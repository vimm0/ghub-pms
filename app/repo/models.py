from django.db import models

from app.user.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)


class Repo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self):
        from git import Repo
        from github import Github

        # using username and password
        # g = Github("vimm0", "vim9815510732")

        import ipdb
        ipdb.set_trace()
        # or using an access token
        g = Github("c435e9c77b942e0220b313404667b2b1b4fcc8b5")

        for repo in g.get_user().get_repos():
            print(repo.name)
            # repo.edit(has_wiki=False)

        pass
