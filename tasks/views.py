from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Count
from django.utils import timezone
from .models import Task, Category, TaskComment, Label

def home(request):
    tasks = Task.objects.filter(completed=False)
    
    # Handle search
    search_query = request.GET.get('search', '')
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Handle filtering
    category_id = request.GET.get('category')
    priority = request.GET.get('priority')
    sort = request.GET.get('sort', '-created_date')
    
    if category_id:
        tasks = tasks.filter(category_id=category_id)
    if priority:
        tasks = tasks.filter(priority=priority)
    
    # Handle sorting
    if sort in ['title', '-title', 'due_date', '-due_date', 'priority', '-priority']:
        tasks = tasks.order_by(sort)
    
    categories = Category.objects.all()
    context = {
        'tasks': tasks,
        'categories': categories,
        'priorities': Task.PRIORITY_CHOICES,
        'selected_category': category_id,
        'selected_priority': priority,
        'selected_sort': sort,
        'search_query': search_query,
    }
    return render(request, 'index.html', context)

def completed(request):
    tasks = Task.objects.filter(completed=True).order_by('-created_date')
    categories = Category.objects.all()
    context = {
        'tasks': tasks,
        'categories': categories,
        'priorities': Task.PRIORITY_CHOICES,
    }
    return render(request, 'completed.html', context)

def remaining(request):
    tasks = Task.objects.filter(completed=False, due_date__isnull=False).order_by('due_date')
    overdue_tasks = [task for task in tasks if task.is_overdue()]
    upcoming_tasks = [task for task in tasks if not task.is_overdue()]
    
    context = {
        'overdue_tasks': overdue_tasks,
        'upcoming_tasks': upcoming_tasks,
        'categories': Category.objects.all(),
        'priorities': Task.PRIORITY_CHOICES,
    }
    return render(request, 'remaining.html', context)

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        category_id = request.POST.get('category')
        
        if title:
            task = Task.objects.create(
                title=title,
                description=description,
                due_date=due_date if due_date else None,
                priority=priority,
                category_id=category_id if category_id else None
            )
            messages.success(request, 'Task added successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Title is required!')
    
    context = {
        'categories': Category.objects.all(),
        'priorities': Task.PRIORITY_CHOICES,
    }
    return render(request, 'add_task.html', context)

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('home')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title', task.title)
        task.description = request.POST.get('description', task.description)
        task.priority = request.POST.get('priority', task.priority)
        task.category_id = request.POST.get('category') or None
        due_date = request.POST.get('due_date')
        task.due_date = due_date if due_date else None
        task.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('home')
    
    context = {
        'task': task,
        'categories': Category.objects.all(),
        'priorities': Task.PRIORITY_CHOICES,
    }
    return render(request, 'task_detail.html', context)

def manage_categories(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color', 'blue')
        if name:
            Category.objects.create(name=name, color=color)
            messages.success(request, 'Category added successfully!')
        else:
            messages.error(request, 'Category name is required!')
    
    categories = Category.objects.all()
    return render(request, 'manage_categories.html', {'categories': categories})

def dashboard(request):
    tasks = Task.objects.all()
    categories = Category.objects.annotate(task_count=Count('task'))
    
    # Calculate statistics
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = total_tasks - completed_tasks
    
    # Calculate priority distribution
    high_priority = tasks.filter(priority='high').count()
    medium_priority = tasks.filter(priority='medium').count()
    low_priority = tasks.filter(priority='low').count()
    
    # Calculate category percentages
    for category in categories:
        category.percentage = (category.task_count / total_tasks * 100) if total_tasks > 0 else 0
    
    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'categories': categories,
        'high_priority': high_priority,
        'medium_priority': medium_priority,
        'low_priority': low_priority,
    }
    return render(request, 'dashboard.html', context)

def profile(request):
    tasks = Task.objects.all()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    
    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'profile.html', context)

def add_comment(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        content = request.POST.get('content')
        if content:
            TaskComment.objects.create(task=task, content=content)
    return redirect('task_detail', task_id=task_id)

def manage_labels(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        if name and color:
            Label.objects.create(name=name, color=color)
            messages.success(request, 'Label created successfully!')
        else:
            messages.error(request, 'Label name and color are required!')
    
    labels = Label.objects.all()
    return render(request, 'manage_labels.html', {'labels': labels})

def delete_label(request, label_id):
    if request.method == 'POST':
        label = get_object_or_404(Label, id=label_id)
        label.delete()
        messages.success(request, 'Label deleted successfully!')
    return redirect('manage_labels')

def edit_label(request, label_id):
    label = get_object_or_404(Label, id=label_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        if name and color:
            label.name = name
            label.color = color
            label.save()
            messages.success(request, 'Label updated successfully!')
            return redirect('manage_labels')
    return render(request, 'edit_label.html', {'label': label})

def calendar_view(request):
    import calendar
    from datetime import datetime, timedelta

    # Get current year and month
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))

    # Create calendar
    cal = calendar.monthcalendar(year, month)
    current_month = datetime(year, month, 1)
    
    # Get tasks for the month
    start_date = current_month
    end_date = (current_month + timedelta(days=32)).replace(day=1)
    tasks = Task.objects.filter(due_date__range=(start_date, end_date))

    # Organize tasks by day
    task_dict = {}
    for task in tasks:
        day = task.due_date.day
        if day not in task_dict:
            task_dict[day] = []
        task_dict[day].append(task)

    # Create calendar data with tasks
    calendar_data = []
    for week in cal:
        week_data = []
        for day in week:
            if day != 0:
                week_data.append((day, task_dict.get(day, [])))
            else:
                week_data.append((day, []))
        calendar_data.append(week_data)

    context = {
        'calendar_data': calendar_data,
        'current_month_name': current_month.strftime('%B'),
        'current_year': year,
        'current_day': datetime.now().day if month == datetime.now().month else 0,
        'prev_month': (month - 1) if month > 1 else 12,
        'prev_year': year if month > 1 else year - 1,
        'next_month': (month + 1) if month < 12 else 1,
        'next_year': year if month < 12 else year + 1,
        'days_of_week': ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    }
    return render(request, 'calendar.html', context)