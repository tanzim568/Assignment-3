from django.shortcuts import render,redirect
from .forms import CatagoryForm

# Create your views here.


def add_catagory(request):
    
    if request.method == 'POST':
        form=CatagoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_catagory')
        
    else:
        form=CatagoryForm()
    return render(request,'catagoryform.html',{'form':form})
        