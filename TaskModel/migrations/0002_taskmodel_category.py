# Generated by Django 5.1.1 on 2024-12-09 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskCatagoryModel', '0003_alter_taskcatergory_task'),
        ('TaskModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='categories', to='TaskCatagoryModel.taskcatergory'),
        ),
    ]
