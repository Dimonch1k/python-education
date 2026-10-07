# ------- 3 ways to initialize a dictionary -------
person = {
	"name": "Alice",
	"age": 25,
	"city": "Lviv"
}
person = {}
person = dict()

# ------- accessing values -------

person = {
	"name": "Alice",
	"age": 25,
	"city": "Lviv"
}

print(person["name"])
print(person["age"])

# print(person["email"]) # KeyError

# ! if key might not exist, it is safer to use get() method
email = person.get("email")

# also you can provide the message if key not exists
email = person.get("email", "Not provided")

print(email, end="\n\n\n")

# ------- operations -------

person["email"] = "alice@example.com"  # add new key
person["age"] = 26  # update an existing key

del person["city"]  # remove an item
print(person)

# also you can use pop function to delete item safely, it returns a deleted value
age = person.pop("city", None)

print(age)
print(person)

# ------- membership -------

person = {
	"name": "Alice",
	"age": 25
}

if "age" in person:
	print("Age is available")

# "Alice" in person.values()  # to check values

print(len(person), end="\n\n\n")  # check length

# ------- iterating -------

person = {
	"name": "Alice",
	"age": 25
}

# get keys by default
for key in person:
	print(key)

# get values
for value in person.values():
	print(value)

# get keys and values
for key, value in person.items():
	print(key, value)

print()

# ! Dictionaries by default preserve insertion order,
#  but they don't sort it alphabetically or numerically


# ------- nested dictionaries -------

users = {
	"alice": {
		"age": 25,
		"role": "developer"
	},
	"bob": {
		"age": 30,
		"role": "designer"
	}
}

print(users["alice"]["role"])

# ------- updating several values -------

user = {
	"name": "Alice"
}

user.update({
	"age": 25,
	"role": "Developer"
})
print(user, end="\n\n\n")

# ------- comprehensions -------

numbers = [1, 2, 3, 4, 5]

squares = {
	number: number ** 2
	for number in numbers
}

print(squares, end="\n\n\n")

# ------- setdefault() function -------

user = {
	"name": "Alice"
}

age = user.setdefault("age", 18)

print(age)
print(user, end="\n\n\n")

# ------- practice -------

user = {
	"id": 42,
	"name": "Alice",
	"email": "alice@example.com",
	"roles": ["developer", "admin"],
	"active": True
}

print(user["name"])
print(user["email"])
print(user["roles"])

user["active"] = False
user["last_login"] = "2026-09-22"

if user["active"]:
	print(f"{user['name']} can log in", end="\n\n\n")
else:
	print(f"{user['name']} is inactive", end="\n\n\n")

# ------- practice (api/json) -------

response = {
	"status": 200,
	"data": {
		"username": "alice",
		"followers": 150
	}
}

username = response["data"]["username"]
followers = response["data"]["followers"]

print(username)
print(followers)
