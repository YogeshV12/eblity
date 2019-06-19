from django.urls import path

from django.contrib.auth import views as auth_views
from . import views as view

urlpatterns = [
    path('plan/', views.plan_view),
    path('journey/', views.Journey_view),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
]