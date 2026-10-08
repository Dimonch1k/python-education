from typing import Optional, Any

# syntax
# variable: type = value

# ------- variable annotations -------


age: int = 18
name: str = "Alice"
price: float = 19.99
active: bool = True
numbers: list[int]
users: dict[str, int]
names: set[str]
user: tuple[str, int]


# ------- function parameter annotations -------
def greet(name: str):
	print(f"Hello, {name}")


def calculate_area(width: float, height: float):
	return width * height


# ------- return type annotations -------
def add(a: int, b: int) -> int:
	return a + b


# ? syntax
# def function(parameter: type) -> return_type:
# 	pass


def get_username(user_id: int) -> str:
	return "Alice"


# ------- complete function annotation -------
def calculate_total(price: float, tax_rate: float) -> float:
	tax = price * tax_rate
	return price + tax


# ! Type annotations are not runtime enforcement

# ------- Static type checking -------
# A tool such as mypy can analyze:
def add(a: int, b: int) -> int:
	return a + b


result = add("10", "20")
print(result)

# ------- built-in types -------

name: str
age: int
price: float
active: bool
data: bytes

numbers: list[int] = [1, 2, 3]


def total(numbers: list[int]) -> int:
	return sum(numbers)


names: list[str] = ["Alice", "Bob", "Charlie"]

users: dict[str, int] = {
	"Alice": 25,
	"Bob": 30
}

user: tuple[str, int] = ("Alice", 25)

unique_ids: set[int] = {1, 2, 3}


# ------- optional values -------
def find_user(user_id: int) -> str | None:
	pass


def find_user(user_id: int) -> str | None:
	if user_id == 1:
		return "Alice"

	return None


def find_user(user_id: int) -> Optional[str]:
	pass


# ------- real cases -------

# union types
def process(value: int | str) -> None:
	print(value)


# any
def get_data(user_id: int) -> Any:
	print(user_id)


value: Any = get_data(1)

# type aliases
UserId = int

user_id: UserId = 42

type User = dict[str, str]


def create_user(user: User) -> None:
	print(user)


# ------- class attributes -------
class User:
	name: str
	age: int

	def __init__(self, name: str, age: int):
		self.name = name
		self.age = age


# ------- practice -------
def create_user(
	name: str,
	age: int,
	active: bool
) -> dict[str, str | int | bool]:
	return {
		"name": name,
		"age": age,
		"active": active
	}


user = create_user(
	name="Alice",
	age=25,
	active=True
)

print(user)


# ------- practice -------

def get_user_name(user: dict[str, str | int]) -> str:
	return str(user["name"])
