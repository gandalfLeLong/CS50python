#exercice 03

def main():

	grocery_list = {}
	while True:
		try:
			item = input().upper()
		except EOFError:
			break
		except KeyboardInterrupt:
			print("\n")
			break
		else:
			if item in grocery_list:
				grocery_list[item] += 1
			else:
				grocery_list[item] = 1
	print_list(grocery_list)

def print_list(items):
	for item in sorted(items.keys()):
		print(f"{items[item]} {item}")

main()