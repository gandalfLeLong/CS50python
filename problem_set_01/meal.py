#exercice 05

def main():
	string = input("What time is it ? ").lower().strip()
	time = convert(string)
	if 7.00 <= time <= 8.00:
		print("breakfast time")
	elif 12.00 <= time <= 13.00:
		print("lunch time")
	elif 18.00 <= time <= 19.00:
		print("dinner time")

def convert(time):
	hours, minutes = time.split(':')
	hours = float(hours)
	minutes = float(minutes)
	minutes /= 60
	return hours + minutes

if __name__ == "__main__":
	main()
