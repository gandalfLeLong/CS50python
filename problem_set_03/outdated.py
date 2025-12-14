#exercice 04

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
	# Program loop
	while True:
		space_flag = True
		user_date = input("Date: ").title()

		#Checking in wich format the date was inputted
		if "/" in user_date:
			date_list = user_date.split("/")
			space_flag = False
		else:
			date_list = user_date.split(" ")
			if "," not in date_list[1]:
				continue

		#Converting the date in int
		if space_flag:
			if date_list[0] not in months:
				continue
			date_list[1] = date_list[1].rstrip(",")
		try:
			day = int(date_list[1])
			year = int(date_list[2])
			if not space_flag:
				month = int(date_list[0])
			else:
				month = months.index(date_list[0]) + 1
		except ValueError:
			continue

		#checking for logical errors in the date and printing
		if day > 31:
			continue
		elif year < 0 or year > 2025:
			continue
		elif month < 1 or month > 12:
			continue
		else:
			print(f"{year:02}-{month:02}-{day:02}")
			break


main()