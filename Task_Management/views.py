from django.shortcuts import render,redirect
from TaskModel.models import TaskModel
from TaskModel.forms import TaskForm

# Create your views here.

def home(request):
    posts=TaskModel.objects.all()
    print(posts)
    for post in posts:
        for pts in post.categories.all():
            print(pts)
    #     tasks=post.task.all()
    #     for task in tasks:
    #         print(task.taskTitle)
    return render (request,'home.html',{'posts':posts})


def edit(request,id):
    data=TaskModel.objects.get(pk=id)
    # form=TaskModel(instance=data)
    # print(data)
    # form=TaskForm(instance=data)
    
    if request.method =='POST':
        form=TaskForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form=TaskForm(instance=data)
    return render(request,'edit.html',{'form':form})


def delete(request,id):
    post=TaskModel.objects.get(pk=id)
    post.delete()
    return redirect('homepage')