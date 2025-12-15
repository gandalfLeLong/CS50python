#exercide 03

def main():
	string = input("Input: ")
	print(shorten(string))

def shorten(word):
	buffer = ""
	for letter in word:
		if is_a_vowel(letter):
			continue
		else:
			buffer += letter
	return buffer

def is_a_vowel(letter):
	if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
		return True
	elif letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U" or letter == "Y":
		return True
	else:
		return False

if __name__ == "__main__":
	main()