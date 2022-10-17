from django.urls import path, register_converter
from . import views
from django.contrib.auth import views as auth_views

register_converter(views.DateConverter, 'date')


urlpatterns = [
    path('planEntry/<int:pk>/', views.planEntry, name='plan-Entry'),
    path('planEntryShow/<int:pk>/', views.planEnt_show, name='plan-Entry-show'),
    path('line/Plan/show/<int:pk>/', views.linePlan_show, name='line-Plan-Show'),
    path('Plan/layout/', views.Plan_layout, name='Plan-Layout'),
    path('Plan/layout/nav/<date:mydate>/',
         views.Plan_layout_nav, name='Plan-Layout-nav'),
    path('plan/forcast/', views.forcast_table, name='forcast-table'),
    path('plan/line/lock/<int:pk>/', views.plan_line_lock, name='plan-line-lock'),
    path('plan/line/move/<int:pk>/', views.plan_line_move, name='plan-line-move'),
    path('style/', views.load_style, name='ajax_load_style'),  # AJAX
]
