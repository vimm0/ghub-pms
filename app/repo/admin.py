from django.contrib import admin

from app.repo.models import Repo, Category


class CategoryAdmin(admin.ModelAdmin):
    pass


class RepoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Repo, RepoAdmin)
