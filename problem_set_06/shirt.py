import sys
from PIL import Image 


def main():
	if len(sys.argv) < 3:
		sys.exit("Too few command line arguments")
	elif len(sys.argv) > 3:
		sys.exit("Too many command line arguments")
	elif not (sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".png")):
		sys.exit("Not an image file1")
	elif not (sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".png")):
		sys.exit("Not an image file2")
	
	shirt = Image.open("shirt.png")
	photo = Image.open(sys.argv[1])
	photo_size = shirt.size
	photo.resize(photo_size)
	photo.paste(shirt, shirt)
	photo.save(sys.argv[2])



if __name__ == "__main__":
	main()
