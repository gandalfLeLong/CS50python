#exercice 01

def main():
	fuel_percentage = ask_fraction_and_convert("Fraction: ")
	fuel_percentage = round(fuel_percentage)
	if fuel_percentage >= 99:
		print("F")
	elif fuel_percentage <= 1:
		print("E")
	else:
		print(f"{fuel_percentage}%")


def ask_fraction_and_convert(prompt):
	while True:
		try:
			x, y = input(prompt).split("/")
			x = int(x)
			y = int(y)
			if x > y or x < 0 or y < 0:
				continue
		except ValueError:
			continue
		except ZeroDivisionError:
			continue

		res = x / y
		return res * 100

main()