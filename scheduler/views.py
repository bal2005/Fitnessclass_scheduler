from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Schedule

def index(request):
    return render(request, 'index.html')

def schedule(request):
    if request.method == 'POST':
        date = request.POST['date']
        title = request.POST['title']
        Schedule.objects.create(title=title, date=date)
        return redirect('index')
    else:
        date = request.GET.get('date')
        return render(request, 'schedule.html', {'date': date})

def view_schedules(request):
    schedules = Schedule.objects.all()
    return render(request, 'view_schedules.html', {'schedules': schedules})

def delete_schedule(request, schedule_id):
    schedule = Schedule.objects.get(id=schedule_id)
    schedule.delete()
    return redirect('view_schedules')

def clear_all_schedules(request):
    Schedule.objects.all().delete()
    return redirect('view_schedules')

def get_events(request):
    schedules = Schedule.objects.all()
    events = []
    for schedule in schedules:
        events.append({
            'title': schedule.title,
            'start': schedule.date.isoformat()
        })
    return JsonResponse(events, safe=False)