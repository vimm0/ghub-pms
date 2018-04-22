# Generated by Django 2.0.4 on 2018-04-22 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0004_remove_repo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repo',
            old_name='last_modified',
            new_name='git_last_modified',
        ),
        migrations.AddField(
            model_name='repo',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
