fruits = ["apple", "banana", "orange"]
items = []
items = list()

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # orange
# print(fruits[3])  # IndexError
print(fruits[-1])  # orange
print(fruits[-2])  # banana

# Lists are mutable
fruits[1] = "grape"
fruits.append("orange")
fruits.insert(2, "grape")
fruits.remove("apple")
fruit = fruits.pop()  # or pop(index)

print(fruits)
print(len(fruits), end="\n\n\n")

# ---------------------

languages = ["Python", "JavaScript", "Go"]

for language in languages:
	print(language)

for index, language in enumerate(languages):
	print(index, language)

print("Java" not in languages, end="\n\n\n")

# ---------------------

numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)

result = sorted(numbers)

print(result, end="\n\n\n")

# ---------------------

a = [1, 2]
b = [3, 4]

result = a + b

print(result)
print([1, 2] * 3, end="\n\n\n")

# ------- list comprehensions -------

# instead of
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
	squares.append(number ** 2)

# you can write simplified version
squares = [number ** 2 for number in numbers]
print(squares)

even_numbers = [
	number
	for number in numbers
	if number % 2 == 0
]
print(even_numbers, end="\n\n\n")

# ------- practice -------

prices = [25.50, 10.00, 40.75, 15.25]

prices.append(30.00)

prices.remove(10.00)

total = sum(prices)
average = total / len(prices)

print(f"Products: {prices}")
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}", end="\n\n\n")

print(f"Max: {max(prices)}")
print(f"Min: {min(prices)}")
print(f"Sum: {sum(prices)}")
print(f"Length: {len(prices)}")

