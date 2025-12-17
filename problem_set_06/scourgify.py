import sys
import csv


def main():
	if len(sys.argv) < 3:
		sys.exit("Too few command line arguments")
	elif len(sys.argv) > 3:
		sys.exit("Too many command line arguments")
	elif not sys.argv[1].endswith(".csv"):
		sys.exit("Not a CSV file")
	elif not sys.argv[2].endswith(".csv"):
		sys.exit("Not a CSV file")

	old_format = get_csv_input(sys.argv[1])
	new_format = update_csv_format(old_format)
	change_csv(sys.argv[2], new_format)


def get_csv_input(file_path):
	lst = []
	try:
		with open(file_path) as file:
			reader = csv.DictReader(file)
			for row in reader:
				lst.append(row)
	except OSError:
		sys.exit("File does not exist")

	return lst


def update_csv_format(data):
	new_list = []
	for row in data:
		line = {}
		last, first = row["name"].split(",")
		line["first"] = first.strip()
		line["last"] = last
		line["house"] = row["house"]
		new_list.append(line)
	return new_list


def change_csv(file_path, data):
	with open(file_path, "w") as file:
		writter = csv.DictWriter(file, fieldnames=["first", "last", "house"])
		writter.writeheader()
		for line in data:
			writter.writerow(line)


if __name__ == "__main__":
	main()