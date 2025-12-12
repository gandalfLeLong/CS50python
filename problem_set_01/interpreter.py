#exercice04
def main():
	string = input("Expression: ").lower().strip()
	x, sign, y = string.split()
	x = float(x)
	y = float(y)
	if (sign == "+"):
		print(f"{x + y:.1f}")
	elif (sign == "-"):
		print(f"{x - y:.1f}")
	elif (sign == "*"):
		print(f"{x * y:.1f}")
	elif (sign == "/"):
		print(f"{x / y:.1f}")
	else:
		print("sign error")

main()