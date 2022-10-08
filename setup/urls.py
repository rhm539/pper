from django.urls import path
from . import views

urlpatterns = [
    path('daily', views.daily, name='daily'),
    path('weekly', views.weekly),
    path('monthly', views.monthly),
]