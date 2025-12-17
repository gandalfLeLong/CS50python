import sys
import csv
import tabulate


def main():
	if len(sys.argv) < 2:
		sys.exit("Too few command line arguments")
	elif len(sys.argv) > 2:
		sys.exit("Too many command line arguments")
	elif not sys.argv[1].endswith(".csv"):
		sys.exit("Not a CSV file")

	menu = get_dics_from_file(sys.argv[1])
	print(menu)
	print(tabulate.tabulate(menu, tablefmt="grid", headers="keys"))


def get_dics_from_file(file_path):
	lst = []
	try:
		with open(file_path) as file:
			reader = csv.DictReader(file)
			for row in reader:
				lst.append(row)
	except OSError:
		sys.exit("File does not exist")

	return lst


if __name__ == "__main__":
	main()