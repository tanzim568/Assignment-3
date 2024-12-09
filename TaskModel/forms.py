from django import forms
from .models import TaskModel  
from TaskCatagoryModel.models import TaskCatergory 


class TaskForm(forms.ModelForm):
   
    class Meta:
        model=TaskModel
        fields='__all__'
        
        labels={
            'Task_Assign_data':"Assigned Date",
            'taskTitle':'Title',
            'taskDescription':'Description',
        }
    
        
        widgets={
            'Task_Assign_data':forms.DateInput(attrs={'type':'date'}),
            'categories':forms.CheckboxSelectMultiple(),
        }
