import unittest
from rental import Rental
from movie import Movie, PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.new_release)
		self.regular_movie = Movie("CitizenFour", PriceCode.normal)
		self.childrens_movie = Movie("Frozen", PriceCode.childrens)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.normal)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.normal, m.get_price_code())

	def test_rental_price(self):
		"""test get_price method"""
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.regular_movie, 4)
		self.assertEqual(rental.get_price(), 5.0)
		rental = Rental(self.childrens_movie, 7)
		self.assertEqual(rental.get_price(), 7.5)

	def test_rental_points(self):
		"""test get_frequent_renter_points method"""
		rental = Rental(self.childrens_movie, 4)
		self.assertEqual(rental.get_frequent_renter_points(), 1)
		rental = Rental(self.regular_movie, 4)
		self.assertEqual(rental.get_frequent_renter_points(), 1)		
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_frequent_renter_points(), 1)
		rental = Rental(self.new_movie, 4)
		self.assertEqual(rental.get_frequent_renter_points(), 4)