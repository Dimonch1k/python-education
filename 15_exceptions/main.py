import InsufficientBalanceError

# Syntax
try:
	number = int(input("Enter a number: "))
except ValueError:
	print("Invalid number.")

# This is preferable to:
try:
	number = int(input("Enter a number: "))
except:
	print("Something went wrong.")

# A bare except catches almost everything, including exceptions you may not intend to handle.


# ------- multiple except blocks -------
try:
	a = int(input("First number: "))
	b = int(input("Second number: "))
	result = a / b

except ValueError:
	print("Please enter numbers.")

except ZeroDivisionError:
	print("You cannot divide by zero.")

# ------- catching multiple exception types -------
try:
	number = int(input("Number: "))
except (ValueError, TypeError):
	print("Invalid value.")

# ------- getting the exception object -------
try:
	number = int("hello")
except ValueError as error:
	print(error)

# ------- else block -------
# The else block runs only if the try block completed without an exception:
try:
	number = int(input("Enter a number: "))
except ValueError:
	print("Invalid input.")
else:
	print(f"You entered {number}.")

# ------- finally block -------
# The finally block executes regardless of whether an exception occurred:
try:
	file = open("./15_exceptions/data.txt")
except FileNotFoundError:
	print("File not found.")
finally:
	print("Operation finished.")

# real world example
file = open("./15_exceptions/data.txt")

try:
	content = file.read()
finally:
	file.close()

# ! For files specifically, Python usually provides an even better approach:
#   with, which automatically manages the resource

try:
	number = int(input("Enter a number: "))
except ValueError:
	print("Invalid number.")
else:
	print(f"Valid number: {number}")
finally:
	print("Finished.")


# ------- raise keyword -------
def withdraw(balance, amount):
	if amount > balance:
		raise ValueError("Insufficient balance")

	return balance - amount


withdraw(250, 200)


# ------- custom exceptions -------
def withdraw(balance, amount):
	if amount > balance:
		raise InsufficientBalanceError("Insufficient balance")

	return balance - amount


try:
	withdraw(250, 200)
except InsufficientBalanceError as error:
	print(error)


# ------- practice -------

def load_config(filename):
	try:
		with open(filename) as file:
			data = file.read()

	except FileNotFoundError:
		print(f"Configuration file '{filename}' was not found.")
		return None

	except PermissionError:
		print(f"Permission denied: '{filename}'.")
		return None

	else:
		print("Configuration loaded successfully.")
		return data


config = load_config("./15_exceptions/data.txt")

if config is not None:
	print(config)
