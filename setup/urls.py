from django.urls import path
from . import views

urlpatterns = [
    path('buyer/list', views.buyer_list,
         name='buyer-list'),  # List and Add Buyer
    path('buyer/edit/<int:pk>/', views.buyer_edit,
         name='buyer-edit'),  # List and Add Buyer
]
