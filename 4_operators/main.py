# ------ Arithmetic Operators
print("Arithmetic Operators:")

a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
print(a // b)  # 3
print(a % b)  # 1
print(a ** b)  # 1000

# ------ Comparison Operators
print("\n\nComparison Operators:")

age = 18

print(age == 18)  # True
print(age != 18)  # False
print(age > 16)  # True
print(age < 16)  # False
print(age >= 18)  # True
print(age <= 18)  # True

# ------ Logical Operators
print("\n\nLogical Operators:")

age = 20
has_ticket = True

print(age >= 18 and has_ticket)
print(age >= 18 or has_ticket)
print(not has_ticket)

# ------ Assignment Operators

x = 5
x += 3  # x = x + 3
x -= 2  # x = x - 2
x *= 4  # x = x * 4
x /= 2  # x = x / 2
x //= 3  # x = x // 3
x %= 2  # x = x % 2
x **= 3  # x = x ** 3

# ------ Membership Operators
print("\n\nMembership Operators:")

fruits = ["apple", "banana", "orange"]

print("apple" in fruits)
print("pear" not in fruits)

text = "Hello Python"

print("Python" in text)  # True

# ----- Identity Operators
print("\n\nIdentity Operators:")

a = [1, 2]
b = a

print(a is b)  # True

a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False

# ----- Bitwise Operators
print("\n\nBitwise Operators:")

a = 6  # 110
b = 3  # 011

print(a & b)  # 2
print(a | b)  # 7
print(a ^ b)  # 5
print(~a)  # -7
print(a << 1)  # 12
print(a >> 1)  # 3

# ---------------------
print("\n\nPractice:")

price = 75
quantity = 2
is_member = True

total = price * quantity

free_shipping = total >= 100 or is_member

print(f"Total: ${total}")
print(f"Free shipping: {free_shipping}")
