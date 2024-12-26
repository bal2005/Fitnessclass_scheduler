from django.contrib import admin
from django.urls import path
from scheduler import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('schedule/', views.schedule, name='schedule'),
    path('view_schedules/', views.view_schedules, name='view_schedules'),
    path('delete_schedule/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),
    path('clear_all_schedules/', views.clear_all_schedules, name='clear_all_schedules'),
    path('get_events/', views.get_events, name='get_events'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)