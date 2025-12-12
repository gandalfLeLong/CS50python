# Converting :) and :( to smileys in unicode

def convert(string):
	string = string.replace(":)", "🙂")
	string = string.replace(":(", "🙁")
	return string

def main():
	string = input()
	string = convert(string)
	print(string)

main()