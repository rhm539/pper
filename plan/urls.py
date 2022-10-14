from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('planEntry/<int:pk>/', views.planEntry, name='plan-Entry'),
    path('style/', views.load_style, name='ajax_load_style'),  # AJAX
]
