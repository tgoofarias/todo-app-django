# Generated by Django 4.2.1 on 2023-05-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('tasks', '0003_tasklist_contributors_tasklist_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='contributors',
            field=models.ManyToManyField(related_name='contributed_task_lists', to='users.profile'),
        ),
    ]