
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='homepage'),
    path('taskmodel/', include('TaskModel.urls')),
    path('taskcategory/', include('TaskCatagoryModel.urls')),
    path('tasks/', include('TaskModel.urls')),
    path('tasks/edit/<int:id>',views.edit,name='edit_task'),
    path('tasks/delete/<int:id>', views.delete,name='delete_task'),
    
]
