#exercice 01

def main():
	fuel_percentage = convert(input("Fraction: "))
	print(gauge(fuel_percentage))


def convert(fraction):
	x, y = fraction.split("/")
	x = int(x)
	y = int(y)
	if y == 0:
		raise ZeroDivisionError
	if x > y or x < 0 or y < 0:
		raise ValueError

	res = x / y
	return round(res * 100)


def gauge(percentage):
	if percentage >= 99:
		return("F")
	elif percentage <= 1:
		return("E")
	else:
		return(f"{percentage}%")


if __name__ == "__main__":
    main()
