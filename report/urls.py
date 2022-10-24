
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('report/day/production/<str:unit>/', views.report_day_production,
         name='report-day-production'),
    path('report/day/production/nav/<date:mydate>/<str:unit>/', views.report_day_production_nav,
         name='report-day-production-nav'),
    path('report/mail/<date:mydate>/', views.report_mail, name='report-mail'),
    path('report/mail/v/<date:mydate>/',
         views.report_mail_view, name='report-mail-view'),
]
