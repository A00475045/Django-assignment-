from django.db import models

class Hotel(models.Model):
    hotelID = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=255)
    hotel_location = models.CharField(max_length=255)
    reviews_in_stars = models.IntegerField(null=True, blank=True)
    total_rooms = models.IntegerField(null=True, blank=True)
    available_rooms = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel_name

    class Meta:
        db_table = 'hotel'
