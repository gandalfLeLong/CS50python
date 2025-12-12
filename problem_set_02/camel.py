# turning all the string from camelCase to snake_case

def main():
	string = input("CamelCase : ").strip()
	string = convert(string)
	print(string)

def convert(string):
	buffer = ""
	for letter in string:
		if letter.isupper():
			buffer += "_" + letter.lower()
		else:
			buffer += letter
	return buffer

main()