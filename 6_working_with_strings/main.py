name = "Dmytro"
message = "Hello, " + name

print(message)

# ---------------------

name = "Dmytro"
language = 'Python'

text = """This is
a multi-line
string."""

message = "He said 'hello'"

# ---------------------

word = "Python"

print(word[0])
print(word[1])
print(word[-1])

print(word[0:3])
print(word[2:6])

print(word[::2])

# ! Strings are immutable, so you cannot change a character in a string
# word[0] = "J" # Type Error

# ! Instead, create new string
word = "Python"
word = "J" + word[1:]

print(word)

# ---------------------

first_name = "Dmytro"
last_name = "Leskiv"

full_name = first_name + " " + last_name

print(full_name)

print("ha" * 3)

print(len(word), end="\n\n\n")

# ---------------------

string = "Python is great"

print("Python" in string)
print("Java" in string)

print(string.find("Python"), end="\n\n\n")

# ---------------------

text = "  Hello Python  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Python", "World"), end="\n\n\n")

# ---------------------

string = "  Python is great  "

print(string.upper())
print(string.lower())
print(string.strip())
print(string.replace("Python", "World"))
print(string.split(" "))
print(" ".join(["Python", "is", "great"]))
print(string.startswith("Python"))
print(string.endswith("great"))
print(string.find("Python"))
print(string.count("Python"), end="\n\n\n")

# ---------------------

name = "Dmytro"
age = 18

message = f"{name} is {age} years old."

print(message)

price = 50
quantity = 3

print(f"Total: ${price * quantity}", end="\n\n\n")

# ---------------------

username = input("Enter your username: ")

username = username.strip().lower()

if " " in username:
	print("Username cannot contain spaces.")
else:
	print(f"Username: {username}")
	print(f"Length: {len(username)}")
