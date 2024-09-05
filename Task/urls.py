from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('addtask', addtask, name='addtask'),
    path('edit/<int:id>', edit, name='edit'),
    path('addtask/<int:id>', Delete, name='Delete'),
    path('task_details/<int:id>', task_details, name='task_details'),
]