# Generated by Django 5.1.1 on 2024-12-09 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskCatagoryModel', '0004_alter_taskcatergory_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcatergory',
            name='task',
        ),
    ]
