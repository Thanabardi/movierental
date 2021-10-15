from movie import Movie, PriceCode

class Rental:
	"""
	A self.of a movie by customer.
	From Fowler's refactoring example.

	A realistic self.would have fields for the dates
	that the movie was rented and returned, from which the
	self.period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""
	
	def __init__(self, movie, days_rented): 
		"""Initialize a new movie self.object for
		   a movie with known self.period (daysRented).
		"""
		self.movie = movie
		self.days_rented = days_rented

	def get_movie(self):
		return self.movie

	def get_days_rented(self):
		return self.days_rented

	def get_price(self):
		return self.movie.price_code.get_charge(self.days_rented)

	def get_frequent_renter_points(self):
		return self.movie.price_code.frequent_renter_points(self.days_rented)