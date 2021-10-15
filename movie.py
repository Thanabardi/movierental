from enum import Enum


class PriceCode(Enum):
	"""An enumeration for different kinds of movies and their behavior"""
	new_release = { "price": lambda days: 3.0*days, 
					"frp": lambda days: days
				}
	normal = { "price": lambda days: 2 + (1.5 * (days-2)) if days > 2 else 2,
					"frp": lambda days: 1
			}
	childrens = { "price": lambda days: 1.5 + (1.5 * (days-3)) if days > 3 else 1.5, 
					"frp": lambda days: 1
			}

	def get_charge(self, days: int) -> float:
		"Return the rental price for a given number of days"""
		pricing = self.value["price"]    # the enum member's price formula
		return pricing(days)

	def frequent_renter_points(self, days: int) -> float:
		"Return the rental price for a given number of days"""
		frp = self.value["frp"]    # the enum member's frequent renter points
		return frp(days)


class Movie:
	"""
	A movie available for rent.
	"""
	# The types of movies (price_code). 
	
	def __init__(self, title, price_code):
		# Initialize a new movie.
		if not isinstance(price_code, PriceCode):
			raise TypeError("price_code must be in PriceCode")
		self.title = title
		self.price_code = price_code

	def get_price_code(self):
		# get the price code
		return self.price_code
	
	def get_title(self):
		return self.title

	# def get_charge(self, days_rented: int):
	# 	amount = 0
	# 	if self.price_code == Movie.REGULAR:
	# 		# Two days for $2, additional days 1.50 each.
	# 		amount = 2.0
	# 		if days_rented > 2:
	# 			amount += 1.5*(days_rented-2)
	# 	elif self.price_code == Movie.CHILDRENS:
	# 		# Three days for $1.50, additional days 1.50 each.
	# 		amount = 1.5
	# 		if days_rented > 3:
	# 			amount += 1.5*(days_rented-3)
	# 	elif self.price_code == Movie.NEW_RELEASE:
	# 		# Straight per day charge
	# 		amount = 3*days_rented
	# 	else:
	# 		log = logging.getLogger()
	# 		log.error(f"Movie {self.title} has unrecognized priceCode {self.price_code}")
	# 	return amount

	# def frequent_renter_points(self, days_rented: int):
	# 	if self.price_code == Movie.NEW_RELEASE and days_rented > 1:
	# 		return 2
	# 	else:
	# 		return 1
	
	def __str__(self):
		return self.title
