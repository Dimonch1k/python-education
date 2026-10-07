# ! A set is a collection where membership and uniqueness matter more than position.

numbers = {1, 2, 2, 3, 3, 3}

print(numbers)  # has only unique values

visitors = [
	"Alice",
	"Bob",
	"Alice",
	"Charlie",
	"Bob"
]

unique_visitors = set(visitors)

print(unique_visitors, end="\n\n\n")

# ------- 3 ways to initialize a set -------

languages = {"Python", "Go", "Rust"}
languages = set()
languages = {}

# ! ------- no indexing -------
# print(numbers[0]) # error

# instead use this
for number in numbers:
	print(number)

print("\n")

# ! ------- membership is important -------
languages = {"Python", "JavaScript", "Go"}

print("Python" in languages)
print("Java" in languages, end="\n\n\n")

# ------- methods -------
numbers.add(10)
numbers.update([10, 20, 30])
numbers.remove(10)
numbers.discard(10)  # remove without giving error
value = numbers.pop()  # remove arbitrary element

print(numbers)
print(value)

numbers.clear()
print(numbers)

numbers = {10, 20, 30}

print(len(numbers), end="\n\n\n")

# ------- union operation -------
python = {"Alice", "Bob", "Charlie"}
go = {"Bob", "David", "Eve"}

result = python | go
# or
result = python.union(go)

print(f"Union: {result}", end="\n\n\n")

# ------- intersection operation -------
python = {"Alice", "Bob", "Charlie"}
go = {"Bob", "David", "Charlie"}

result = python & go
# or
result = python.intersection(go)

print(f"Intersection: {result}", end="\n\n\n")

# ------- difference -------
python = {"Alice", "Bob", "Charlie"}
go = {"Bob", "David"}

result = python - go
# or
result = python.difference(go)

print(f"Difference: {result}", end="\n\n\n")

# ------- symmetric difference -------
python = {"Alice", "Bob", "Charlie"}
go = {"Bob", "David"}

result = python ^ go
# or
result = python.symmetric_difference(go)

print(f"Symmetric difference: {result}", end="\n\n\n")

# ------- subset and superset -------
backend = {"Python", "SQL"}
skills = {"Python", "SQL", "Docker", "Linux"}

resultSubset = backend <= skills
# or
resultSubset = backend.issubset(skills)

resultSuperset = backend >= skills
# or
resultSuperset = backend.issuperset(skills)

print(f"Subset: {resultSubset}", end="\n\n")
print(f"Superset: {resultSuperset}", end="\n\n\n")

# ------- practice -------

python_students = {
	"Alice",
	"Bob",
	"Charlie",
	"David"
}

web_students = {
	"Bob",
	"Charlie",
	"Eve"
}

both = python_students & web_students
all_students = python_students | web_students
only_python = python_students - web_students

print(f"Both: {both}")
print(f"All students: {all_students}")
print(f"Only python: {only_python}")
