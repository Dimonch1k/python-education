my_name = "Dmytro"
age = 25

print(f"Hello, {my_name}!")

if age >= 18:
	print("Adult")

# ---------------------

value = 10
value = "hello"
print(value)


# ---------------------

def greet(name):
	return f"Hello, {name}!"


name = input("Your name: ")
message = greet(name)

print(message)
