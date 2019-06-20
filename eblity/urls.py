from django.urls import path,re_path

from . import views

urlpatterns = [
    path('plan/', views.plan_view),
    path('journey/', views.Journey_view),
    path('attendance/', views.attendance_view),
    # re_path(r'^attendance/(?P<date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/$', views.index, name='update_data'),)
  
]