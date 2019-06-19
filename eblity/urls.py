from django.urls import path

from . import views

urlpatterns = [
    path('plan/', views.plan_view),
    path('journey/', views.Journey_view),
    path('attendance/', views.attendance_view),  
]