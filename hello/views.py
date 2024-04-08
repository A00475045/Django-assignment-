from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel
from .serializers import HotelSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics


class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetail(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelList(APIView):
    """
    List all hotels, or create a new hotel.
    """
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelDetail(APIView):
    """
    Retrieve a hotel instance.
    """
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
