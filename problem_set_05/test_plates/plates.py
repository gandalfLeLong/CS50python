#Exercice 04

def main():
	plate = input("Plate: ").upper()
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")

def is_valid(s):
	if start_with_two_letters(s):
		return False
	elif min_max_char(s):
		return False
	elif number_check(s):
		return False
	elif special_char_check(s):
		return False
	else:
		return True

def start_with_two_letters(s):
	s = s[0:2]
	return not s.isalpha()

def min_max_char(s):
	return not (2 <= len(s) <= 6)

def number_check(s):
	number_flag = False
	first_number = True
	for letter in s:
		if letter.isdecimal():
			number_flag = True
			if first_number == True:
				if letter == "0":
					return True
				first_number = False
		elif number_flag == True and letter.isalpha():
			return True

def special_char_check(s):
	return not s.isalnum()

if __name__ == "__main__":
	main()