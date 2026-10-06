age = 16

if age >= 18:
	print("Adult")
else:
	print("Minor")

# ---------------------

score = 75

if score >= 90:
	grade = "A"
elif score >= 80:
	grade = "B"
elif score >= 70:
	grade = "C"
else:
	grade = "D"

print(grade)

# ---------------------

age = 25
has_ticket = True

if age >= 18 and has_ticket:
	print("Entry allowed")

if age < 18 or not has_ticket:
	print("Entry denied")

if age >= 18:
	if has_ticket:
		print("Entry allowed")

# ---------------------

name = ""

if name:
	print("Name provided")
else:
	print("Name is empty")

# ---------------------

command = "start"

match command:
	case "start":
		print("Starting...")
	case "stop":
		print("Stopping...")
	case "restart":
		print("Restarting...")
	case _:
		print("Unknown command")

# ---------------------

status = 404

match status:
	case 200:
		print("OK")
	case 404:
		print("Not Found")
	case 500:
		print("Server Error")
	case _:
		print("Unknown status")

# ---------------------

age = int(input("Enter your age: "))
is_member = input("Are you a member? (yes/no): ")

if age < 18:
	print("Access denied.")
elif is_member == "yes":
	print("Member access granted.")
else:
	print("Regular access granted.")

# ---------------------

command = input("Command: ")

match command:
	case "start":
		print("Server started")
	case "stop":
		print("Server stopped")
	case "status":
		print("Server is running")
	case _:
		print("Unknown command")
