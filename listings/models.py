
from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=255)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.guest_name} - {self.listing.title}"
