from django.contrib import admin
from django.utils.safestring import mark_safe

from app.repo.models import Repo, Category


class RepoAdmin(admin.ModelAdmin):
    list_display = ('name', 'repo_full_name', 'category', 'size', 'git_last_modified')
    # fields = ('name',)
    # readonly_fields = ('kk',)

    readonly_fields = (
        'name', 'category', 'repo_full_name', 'owner_name', 'owner_username', 'language', 'git_last_modified',
        'created', 'size', 'description', 'clone_link', 'issues_link', 'merges_link', 'milestones_link', 'comments_link',
        'commits_link')
    fields = ('name', 'category', 'repo_full_name', 'owner_name', 'owner_username', 'language', 'git_last_modified',
              'created', 'size', 'description', 'clone_link', 'issues_link', 'merges_link', 'milestones_link', 'comments_link',
        'commits_link')

    def clone_link(self, instance):
        return mark_safe('<a href="%s">%s</a>' % (instance.clone_url, instance.clone_url))

    def issues_link(self, instance):
        return mark_safe('<a href="%s">%s</a>' % (instance.issues_url, instance.issues_url))

    def merges_link(self, instance):
        return mark_safe('<a href="%s">%s</a>' % (instance.merges_url, instance.merges_url))

    def milestones_link(self, instance):
        return mark_safe('<a href="%s">%s</a>' % (instance.milestones_url, instance.milestones_url))

    def comments_link(self, instance):
        return mark_safe('<a href="%s">%s</a>' % (instance.comments_url, instance.comments_url))

    def commits_link(self, instance):
        return mark_safe('<a href="%s">%s</a>' % (instance.commits_url, instance.commits_url))


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
