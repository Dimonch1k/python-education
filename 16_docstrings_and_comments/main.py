# syntax
def greet(name):
	"""Return a greeting for the given name."""
	return f"Hello, {name}!"


print(greet.__doc__)
# or
help(greet)


# ------- class docstrings -------

class User:
	"""Represent a user account."""

	def __init__(self, name):
		self.name = name


print(User.__doc__)

# ------- module docstrings -------
# ! A module can have a docstring at the beginning of the file:
"""Utilities for working with users."""


def create_user(name):
	...


# you can access through
print(__doc__)


# ------- method docstrings -------
class Calculator:
	def add(self, a, b):
		"""Return the sum of two numbers."""
		return a + b


print(Calculator.add.__doc__)


# ------- comments -------

# ! a comment begins with #
# ! triple-quoted strings like this """....""" is not actually a comment

# ! Difference between comments and docstrings

# Docstring
#    ↓
# stored as metadata
#    ↓
# function.__doc__
#    ↓
# documentation tools / help()


# Comment
#    ↓
# ignored by Python interpreter

# ------- help function -------
# Python's built-in help() function can display documentation
def square(number):
	"""Return the square of a number."""
	return number ** 2


help(square)


# ------- practice -------

def calculate_order_total(prices, tax_rate=0.2):
	"""
	Calculate the total price of an order including tax.

	Args:
		prices: A collection of product prices.
		tax_rate: Tax rate represented as a decimal.

	Returns:
		The final order total including tax.
	"""
	subtotal = sum(prices)
	tax = subtotal * tax_rate

	# Tax is calculated from the subtotal, not from individual items.
	return subtotal + tax


prices = [20, 50, 30]

total = calculate_order_total(prices)

print(total)

# ? The docstring explains the function's public purpose and interface.
# ? The comment explains a particular implementation decision.
# ? The code performs the actual operation
