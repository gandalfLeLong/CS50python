#exercice 01

def main():
	string = input("What's the Answer to the Great Question of Life, the Universe, and Everything ? ").lower().strip()
	if string == "42":
		print("Yes")
	elif string == "forty-two" or string == "forty two":
		print("Yes")
	else:
		print("No")

main()