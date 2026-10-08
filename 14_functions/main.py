# syntax

def greet(parameter1, parameter2, parameter3):
	print("Hello!")


# ------- function parameters -------
def greet(name):
	print(f"Hello, {name}!")
	return f"Hello, {name}!"  # returns some data from the function


print(greet("Alice"))


# ! Parameter → variable defined by the function
# ! Argument  → actual value supplied when calling it

# ------- default parameters -------
def greet(name, greeting="Hello"):
	print(f"{greeting}, {name}!")


greet("Alice")
greet("Alice", "Welcome")


# ------- keyword arguments -------
def create_user(name, age):
	print(name, age)


create_user(name="Alice", age=25)

# also we can change the order of arguments

create_user(age=25, name="Alice")


# ------- variable-length arguments -------
# *args collects positional arguments into a tuple
def add_all(*numbers):
	return sum(numbers)


print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40))


# **kwargs collects keyword arguments into a dictionary

def show_user(**user):
	print(user)


show_user(name="Alice", age=25)


# ------- scope -------
# ! Variables created inside a function normally belong to that function's local scope
def calculate():
	result = 10 + 20
	print(result)


calculate()


# print(result)  # NameError

# ------- functions can call other functions -------
def calculate_tax(price):
	return price * 0.2


def calculate_total(price):
	tax = calculate_tax(price)
	return price + tax


print(calculate_total(100), end="\n\n\n")


# ------- type hints -------
# ! The annotations help humans, IDEs, type checkers, and documentation tools,
#   but Python generally does not enforce them at runtime
def add(a: int, b: int) -> int:
	return a + b


# ------- practice -------
def calculate_total(price, tax_rate=0.2):
	tax = price * tax_rate
	return price + tax


product1 = calculate_total(100)
product2 = calculate_total(250)
product3 = calculate_total(50)

print(product1)
print(product2)
print(product3, end="\n\n\n")


# ------- practice -------
def calculate_order_total(prices, tax_rate=0.2):
	subtotal = sum(prices)
	tax = subtotal * tax_rate
	total = subtotal + tax

	return total


prices = [20, 50, 30]

total = calculate_order_total(prices)

print(f"Total: ${total:.2f}")
