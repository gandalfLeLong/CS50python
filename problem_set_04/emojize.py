import emoji

def main():
	string = input("Input: ").strip()
	print(emoji.emojize("Output: " + string, language="alias"))

main()