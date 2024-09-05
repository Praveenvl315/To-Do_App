from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'home.html', context)

def task_details(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task
    }
    return render(request, 'task_details.html', context)

def addtask(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        Task.objects.create(title=title, desc=desc)
        return redirect('home')

    return render(request, 'addtask.html')

def edit(request, id):
    # getting particular data to modify
    task = Task.objects.get(id=id)
    
    # getting data from post mode to edit
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']

        # saving changes in DB from above variable 
        task.title = title
        task.desc = desc
        task.save()

        return redirect('home')
    return render(request, 'edit.html', { 'task': task })

def Delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')





    
