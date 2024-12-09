from django.shortcuts import render,redirect
from .forms import TaskForm

# Create your views here.


def add_task(request):
    
    if request.method == "POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
            
    else:
        form=TaskForm()
    return render (request,'add_taskform.html',{"form":form})
    