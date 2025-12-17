import sys


def main():
	if len(sys.argv) < 2:
		sys.exit("Too few command line arguments")
	elif len(sys.argv) > 2:
		sys.exit("Too many command line arguments")
	elif not sys.argv[1].endswith(".py"):
		sys.exit("Not a python file")
	
	lines = file_to_list(sys.argv[1])
	count = count_true_lines(lines)
	print(count)


def file_to_list(file_name):

	lines = []
	try :
		with open(sys.argv[1]) as file:
			for line in file:
				lines.append(line.strip())
	except OSError:
		sys.exit("File does not exist")
	return lines	


def count_true_lines(lines):
	count = 0
	for line in lines:
		if line.startswith("#"):
			continue
		elif line == "":
			continue
		else:
			count += 1
	return count


if __name__ == "__main__":
	main()