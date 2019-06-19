from django.urls import path

from django.contrib.auth import views as auth_views
from . import views as views

urlpatterns = [
    path('plan/', views.plan_view),
    path('journey/', views.Journey_view),
    path('login/', views.user_login, name='login',),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register),
    path('attendance/', views.attendance_view),  
]