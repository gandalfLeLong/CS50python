import random

def main():
	lvl = ask_for_positive_int("Level: ")
	secret_number = generate_number(lvl)
	print(secret_number)
	while True:
		guess = ask_for_positive_int("Guess: ")
		if guess < secret_number:
			print("Too small!")
			continue
		elif guess > secret_number:
			print("Too large!")
			continue
		else:
			print("Just right!")
			break


#asking user for input
def ask_for_positive_int(prompt):
	while True:
		try:
			number = int(input(prompt).strip())
		except ValueError:
			continue
		if number < 0:
			continue
		else:
			return number

def generate_number(lvl):
	return random.randint(1, lvl)

if __name__ == "__main__":
	main()