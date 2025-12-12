#exercice 02

def main():
	string = input("Greeting: ").lower().strip()
	if string.startswith("hello"):
		print("$0")
	elif string.startswith("h"):
		print("$20")
	else:
		print("$100")

main()