from django.test import TestCase

from .models import List, Ship, ListShipInclusion

class ListModelTest(TestCase):
    def setUp(self):
        List.objects.create(name="Test List 1", max_points=100)

    def tearDown(arg):
        pass

    def test_list_str(self):
        list = List.objects.get(name="Test List 1")
        self.assertEqual(str(list), "Test List 1")


class ShipModelTest(TestCase):
    def setUp(self):
        Ship.objects.create(name="Test Ship 1", stats="Some string")

    def tearDown(arg):
        pass

    def test_ship_str(self):
        ship = Ship.objects.get(name="Test Ship 1")
        self.assertEqual(str(ship), "Test Ship 1")
