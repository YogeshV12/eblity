from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.schedule),
    path('stitched_start/', views.stitched_start, name = "stitched_start"),
    path('alerts/', views.alert)
]