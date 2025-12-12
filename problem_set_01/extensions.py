# ex03

def main():
	string = input("File name: ").lower().strip()
	if string.endswith(".gif"):
		print("image/gif")
	elif string.endswith(".jpg"):
		print("image/jpeg")
	elif string.endswith(".jpeg"):
		print("image/jpeg")
	elif string.endswith(".png"):
		print("image/png")
	elif string.endswith(".pdf"):
		print("application/pdf")
	elif string.endswith(".txt"):
		print("text/plain")
	elif string.endswith(".zip"):
		print("application/zip")
	else:
		print("application/octet-stream")

main()
