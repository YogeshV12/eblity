from django.urls import path,re_path

from django.contrib.auth import views as auth_views
from . import views as views

urlpatterns = [
    path('plan/', views.plan_view),
    path('journey/', views.Journey_view),
    path('attendance/', views.attendance_view),
    # re_path(r'^attendance/(?P<date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/$', views.index, name='update_data'),)
  
    path('login/', views.user_login, name='login',),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register),
    path('attendance/', views.attendance_view),  
]