point = (10, 20)
point = 10, 20

print(point)

# value = (10) # integer
# value = (10,) # tuple

point = (10, 20, 30)

print(point[0])  # 10
print(point[1])  # 20
print(point[2])  # 30
print(point[-1])  # 30

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

languages = ("Python", "Go", "Rust")

for language in languages:
	print(language)

point = (10, 20)

# point[0] = 50 # TypeError
# point.append(30)  # AttributeError
# point.pop()  # AttributeError

# instead make new tuple
point = (50, point[1])

print(point)

# tuple unpacking
point = (10, 20)

x, y = point

print(x)  # 10
print(y)  # 20


# ------- returning multiple values from a function -------

def get_user():
	return "Alice", 25


name, age = get_user()

print(name)  # Alice
print(age)  # 25

# ------- swapping variables -------

a = 10
b = 20

a, b = b, a

print(a)  # 20
print(b)  # 10

# ------- nested -------

points = (
	(10, 20),
	(30, 40),
	(50, 60)
)
print(points[0][1])

# ---------------------

data = ("Python", [1, 2, 3])

data[1].append(4)

print(data)

# ---------------------

numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))

# ---------------------

numbers = (10, 20, 30)

print(numbers.index(20))

# ---------------------

point = (10, 20)

print(len(point))

# ---------------------

languages = ("Python", "Go", "Rust")

print("Python" in languages)

# ---------------------

numbers = (5, 2, 8, 1)

result = sorted(numbers)

print(result)

# ------- practice -------

point = (150, 300)

x, y = point

print(f"X coordinate: {x}")
print(f"Y coordinate: {y}")


# ------- practice -------

def get_user():
	name = "Alice"
	age = 25
	role = "Developer"

	return name, age, role


name, age, role = get_user()

print(name)
print(age)
print(role)

# ------- practice -------

locations = {
	(49.8397, 24.0297): "Lviv",
	(50.4501, 30.5234): "Kyiv"
}

print(locations[(49.8397, 24.0297)])
