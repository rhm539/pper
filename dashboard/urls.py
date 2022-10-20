from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('<str:unit>/', views.index, name='dashboard-index'),
]
