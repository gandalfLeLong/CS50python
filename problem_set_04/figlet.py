import sys
import random
from pyfiglet import Figlet

def main():

	#check for args validity
	flag_font = False
	if len(sys.argv) != 1 and len(sys.argv) != 3:
		sys.exit("Invalid usage")
	if len(sys.argv) == 3:
		flag_font = True
		if sys.argv[1] != "-f" and sys.argv[1] != "--font":
			sys.exit("Invalid usage")

	#set up figlet
	figlet = Figlet()
	font_list = figlet.getFonts()
	if flag_font:
		if sys.argv[2] in font_list:
			figlet.setFont(font=sys.argv[2])
		else:
			sys.exit("Invalid usage")
	else:
		figlet.setFont(font=random.choice(font_list))

	#user input and rendering
	user_input = input("Input: ")
	print("Output:\n" + figlet.renderText(user_input))



if __name__ == "__main__":
	main()