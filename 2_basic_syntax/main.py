name = "Dmytro"
print(name)

age = 18
height = 1.73

print(type(age))

if age >= 18:
	print("Adult")

# Inline comment

"""
For documentation.
Used by .__doc__
"""

print(name, age)
print(name, " is ", age, " years old")
print(f"{name} is {age} years old")

# ---------------------

name = input("What's your name? ")

print(f"Hello, {name}!")

age = int(input("How old are you? "))

print(age + 1)

# ---------------------

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
	status = "adult"
else:
	status = "minor"

print(f"{name} is {age} years old.")
print(f"Status: {status}")
