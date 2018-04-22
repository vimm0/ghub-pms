from django.contrib import admin

from app.repo.models import Repo, Category


class RepoAdmin(admin.ModelAdmin):
    list_display = ('name', 'repo_full_name', 'category', 'size', 'git_last_modified')


class RepoInline(admin.TabularInline):
    """
    Repository inline
    """
    fieldsets = (
        (
            None,
            {
                'fields': ('name', 'repo_full_name', 'category', 'size', 'git_last_modified',)
            }
        ),
    )

    model = Repo
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (RepoInline,)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Repo, RepoAdmin)
