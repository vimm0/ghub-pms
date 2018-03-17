# Generated by Django 2.0.3 on 2018-03-17 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0002_repo_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='repo',
            name='clone_url',
            field=models.TextField(blank=True, help_text='Do not edit.', null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='repo',
            name='comments_url',
            field=models.TextField(blank=True, help_text='Do not edit.', null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='repo',
            name='commits_url',
            field=models.TextField(blank=True, help_text='Do not edit.', null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='repo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='repo',
            name='issues_url',
            field=models.TextField(blank=True, help_text='Do not edit.', null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='repo',
            name='language',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='repo',
            name='last_modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='repo',
            name='merges_url',
            field=models.TextField(blank=True, help_text='Do not edit.', null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='repo',
            name='milestones_url',
            field=models.TextField(blank=True, help_text='Do not edit.', null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='repo',
            name='owner_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='repo',
            name='owner_username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='repo',
            name='repo_full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='repo',
            name='size',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
