from django.urls import path
from . import views

urlpatterns = [
    path('buyer/list', views.buyer_list,
         name='buyer-list'),  # List and Add Buyer
    path('buyer/edit/<int:pk>/', views.buyer_edit,
         name='buyer-edit'),  # List and Edit Buyer
    path('style/list', views.style_list,
         name='style-list'),  # List and Add Buyer
    path('style/edit/<int:pk>/', views.buyer_edit,
         name='style-edit'),  # List and Edit Buyer
]
