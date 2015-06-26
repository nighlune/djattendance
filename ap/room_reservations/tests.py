import unittest

from django.test import TestCase
from room_reservations.models import Reservation
from rooms.models import Building, Room

from hypothesis.extra.django import TestCase
from hypothesis import given
from hypothesis.extra.django.models import models
from hypothesis.strategies import just, lists


# random creation of an object with relevant data types:
# c = models(Customer).example()

# def set_up_data():
# 	# foreign models
# 	building = Building(name="Training Center", code="TC")
# 	room = Room(building=building, code="NE210")

class ReservationTestCase(TestCase):
	@given(
		lists(models(Reservation, room=models(Room)), min_size=1, max_size=10),
		)

    def test_models(self, res_list):

    	for res in res_list:
    		self.assertTrue(Reservation(res))


class ReservationGroupTestCase(TestCase):

	def setUp(self):
		pass