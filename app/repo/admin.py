from django.contrib import admin

from app.repo.models import Repo


class RepoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Repo, RepoAdmin)
