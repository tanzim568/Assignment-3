from django.db import models
from TaskCatagoryModel.models import TaskCatergory


# Create your models here.


class TaskModel(models.Model):
    taskTitle=models.CharField(max_length=100)
    taskDescription=models.TextField()
    is_completed=models.BooleanField(default=False)
    Task_Assign_data=models.DateField()
    categories=models.ManyToManyField(TaskCatergory)
  
    
    
    def __str__(self):
        return f"title:{self.taskTitle}"