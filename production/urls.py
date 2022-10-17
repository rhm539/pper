from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('line/layout/', views.line_layout, name='Line-Layout'),
    path('hourly/report/entry/<int:pk>/',
         views.hourly_report_entry, name='hourly-report-Entry'),
    path('line/layout/nav/<date:mydate>/',
         views.line_layout_nev, name='line-Layout-nav'),
    path('line/delete/<int:pk>/', views.line_delete, name='line-delete'),
    path('line/lock/<int:pk>/', views.line_lock, name='line-lock'),
]
