import sys

def read_file(filename):
	text = None
	try:
		with open(filename, "r") as f:
			text = f.read().strip()
	except FileNotFoundError:
		print(f"Error: the file {filename} does not exist.")
	finally:
		return text

def obfuscate(filename):
	text = read_file(filename)
	if not text:
		print(f"File {filename} is empty")
		exit(1)

	orded = []
	for char in text:
		orded.append(ord(char))
	print(orded)


if __name__ == "__main__":

	if not len(sys.argv) > 1:
		print("Missing target file")
		exit(1)


	filename = sys.argv[1]
	obfuscate(filename)
