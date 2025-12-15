import random

def main():
	user_score = 0
	lvl = get_level("Level: ")
	problem_list = generate_list(lvl)

	for problem in problem_list:
		res = problem[0] + problem[1]
		if get_res(res, problem[0], problem[1]):
			user_score += 1
	print(f"Score: {user_score}")

def get_level(prompt):
	while True:
		try:
			number = int(input(prompt).strip())
		except ValueError:
			continue
		if number < 1 or number > 3:
			continue
		else:
			return number

def generate_list(lvl):
	problem_list = []
	for i in range(0, 10):
		problem = [generate_integer(lvl), generate_integer(lvl)]
		problem_list.append(problem)
	return problem_list

def generate_integer(lvl):
	if 0 < lvl < 4:
		raise ValueError
	if lvl == 1:
		base = 10
	elif lvl == 2:
		base = 100
	else:
		base = 1000
	return random.randint(0, base)

def	get_res(res, x, y):
	for i in range(0, 3):
		try:
			guess = int(input(f"{x} + {y} = "))
		except ValueError:
			print("EEE")
			if i == 2:
				print(f"{x} + {y} = {res}")
				return False

		if guess == res:
			return True
		else:
			print("EEE")
		if i == 2:
			print(f"{x} + {y} = {res}")
			return False

if __name__ == "__main__":
	main()