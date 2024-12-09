from django.db import models
# from TaskModel.models import TaskModel

# Create your models here.


class TaskCatergory(models.Model):
    category_name=models.CharField(max_length=50)
    #task=models.ManyToManyField('TaskModel',blank=True)
    
    
    
    def __str__(self):
        return self.category_name