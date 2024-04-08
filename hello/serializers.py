from pydantic import generics
from rest_framework import serializers
from .models import Hotel
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotelID', 'hotel_name', 'hotel_location', 'reviews_in_stars', 'total_rooms', 'available_rooms', 'created_at']

