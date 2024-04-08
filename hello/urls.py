from django.urls import path
from . import views

urlpatterns = [
    path('hotels/', views.HotelList.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/', views.HotelDetail.as_view(), name='hotel-detail'),
]