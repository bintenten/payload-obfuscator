import sys

def read_file(filename):
	try:
		with open(filename, "r") as f:
			text = f.read()
		return text
	except FileNotFoundError:
		print(f"Error: the file {filename} does not exist.")

def obfuscate(filename):
	text = read_file(filename)



if __name__ == "__main__":

	if not len(sys.argv) > 1:
		print("Missing target file")
		exit(1)


	filename = sys.argv[1]
	obfuscate(filename)
