import inflect
import sys

def main():
	o = inflect.engine()
	names = []
	while True:
		try:
			names.append(input("Name: ").strip().title())
		except EOFError:
			print()
			break
		except KeyboardInterrupt:
			print()
			break
	print("Adieu, adieu, to", o.join(names))



if __name__ == "__main__":
	main()