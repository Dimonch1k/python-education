# ! Explicit conversion means you manually request a conversion
# ! Implicit conversion means Python automatically handles the conversion between data types without your intervention

# Python does not automatically convert everything
age = 18

# print("Age: " + age)  # TypeError
# instead you should explicitly conver it to string

print("Age: " + str(age))
# or  use f-string
print(f"Age: {age}", end="\n\n\n")

# ! ------- key functions/methods -------

# int()
print(int("100"))
print(int(3.14), end="\n\n")

# float()
print(float("10.5"))
print(float(10), end="\n\n")

# str()
print(str(100))
print(str(3.14), end="\n\n")

# bool()
print(bool(0))
print(bool(10))
print(bool(""))
print(bool("hello"), end="\n\n")

# list()
print(list((1, 2)), end="\n\n")

# tuple()
print(tuple([1, 2]), end="\n\n")

# set()
print(set([1, 2, 2]), end="\n\n")

# dict()
print(dict([("a", 1)]), end="\n\n\n")

# ------- practice -------

a = input("Enter first number: ")
b = input("Enter second number: ")

a = int(a)
b = int(b)

result = a + b

print(f"Result: {result}", end="\n\n")

# or more compact version

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b, end="\n\n\n")

# ------- practice -------

config = {
	"port": "8080",
	"debug": "1"
}

port = int(config["port"])
debug = bool(int(config["debug"]))

print(port)
print(debug)
