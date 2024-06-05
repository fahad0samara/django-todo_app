from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'index.html')
def completed(request):
    return render (request, 'completed.html')

def add_task(request):
    return render(request,"add_task.html" )

def delete_task(request):
    return render(request,"delete.html" )

def remaining(request):
    return render(request,"remaining.html" )

def task_detail(request):
    return render(request,"task_detail.html" )