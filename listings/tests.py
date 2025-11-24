from django.test import TestCase
from .models import Listing, Booking

# Optional: add DRF API tests here
class ListingModelTest(TestCase):
    def setUp(self):
        Listing.objects.create(title="Test Listing", location="Addis Ababa", price=100)

    def test_listing_creation(self):
        listing = Listing.objects.get(title="Test Listing")
        self.assertEqual(listing.location, "Addis Ababa")
        self.assertEqual(listing.price, 100)
