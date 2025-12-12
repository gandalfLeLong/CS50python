#exercide 03

def main():
	string = input("Input: ")
	for letter in string:
		if is_a_vowel(letter):
			continue
		else:
			print(letter, end="")

def is_a_vowel(letter):
	if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
		return True
	elif letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U" or letter == "Y":
		return True
	else:
		return False

main()