# Generated by Django 5.2.2 on 2025-06-10 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jira', '0003_jiratoken_delete_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jiratoken',
            old_name='acess_token',
            new_name='access_token',
        ),
    ]
