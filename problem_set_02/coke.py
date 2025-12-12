#exercice 02

def main():
	total = 0

	while True:
		print(f"Amount due: {50 - total}")
		amount = int(input("Insert coin: "))
		match amount:
			case 25:
				total += 25
			case 10:
				total += 10
			case 5:
				total += 5
			case _:
				continue
		if total >= 50:
			change = total - 50
			print(f"Change Owed: {change}")
			break

main()