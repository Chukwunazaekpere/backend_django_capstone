

from unittest import TestCase
from menu.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Pizza", price=80, inventory=100)
        self.assertEqual(item, "Pizza : 80")