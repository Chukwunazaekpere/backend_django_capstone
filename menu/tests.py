from django.test import TestCase

# Create your tests here.
from .models import (
    Booking,
    Category,
    Menu
)


class MenuTestCases(TestCase):
    def test_booking_returns_fullname(self):
        pass