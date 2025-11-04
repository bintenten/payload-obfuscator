import sys

def obfuscate(filename):
	with open(filename, "r") as f:
		text = f.read()
	print(text)


if __name__ == "__main__":

	if not len(sys.argv) > 1:
		print("Missing target file")
		exit(1)


	filename = sys.argv[1]
	obfuscate(filename)
