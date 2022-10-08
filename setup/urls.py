from django.urls import path
from . import views

urlpatterns = [
    path('buyer/list', views.buyer_list, name='buyer-list'),
    path('weekly', views.weekly),
    path('monthly', views.monthly),
]
