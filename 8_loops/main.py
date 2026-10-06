# ------- for loop -------
languages = ["Python", "JavaScript", "Go"]

for language in languages:
	print(language)

# loop through the string's characters
for character in "Python":
	print(character)

# range function
for i in range(5):
	print(i)

for i in range(2, 11, 2):
	print(i)

# break keyword
for number in range(10):
	if number == 5:
		break

	print(number)

# continue keyword
for number in range(5):
	if number == 2:
		continue

	print(number)

# else after for loop - only if for finished normally
for number in range(3):
	print(number)
else:
	print("Loop finished")

# nested
for x in range(3):
	for y in range(2):
		print(x, y)

# ------- while loop -------
count = 0

while count < 5:
	print(count)
	count += 1

# ! Infinite loop - can drain a lot of resources if used incorrectly
# while True:
# 	print("Running...")


# ------- practice for -------

products = [
	("Keyboard", 80),
	("Mouse", 30),
	("Monitor", 250)
]

total = 0

for name, price in products:
	print(f"{name}: ${price}")
	total += price

print(f"Total: ${total}")

# ------- practice while -------

password = ""

while password != "secret":
	password = input("Enter password: ")

print("Access granted")
