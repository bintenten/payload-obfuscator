import sys
import random

def read_file(filename):
	text = None
	try:
		with open(filename, "r") as f:
			text = f.read().strip()
	except FileNotFoundError:
		print(f"Error: the file {filename} does not exist.")
	finally:
		return text

def write_output(filename, output):
	with open(filename, "w+") as f:
		f.write(output)

def num_parser(num):
	if isinstance(num, str):
		num = int(num)

	mat = []
	org_num = num
	while num != 0:
		rand_int = 0
		if len(mat) == 0:
			rand_int = random.randint(0, num - (num // 2))
		else:
			rand_int = random.randint(0, num)
		if rand_int == 0:
			continue

		num = num - rand_int
		mat.append(rand_int)

	if sum(mat) != org_num:
		mat.append(org_num - sum(mat))

	return mat


def obfuscate(filename, output_file):
	text = read_file(filename)
	if not text:
		print(f"File {filename} is empty")
		exit(1)

	orded = []
	for char in text:
		ord_char = ord(char)
		mat_list = num_parser(ord_char)
		formated_formula = f"({' + '.join([str(num) for num in mat_list])})"
		orded.append(formated_formula)

	output = ' + '.join([str(o) for o in orded])

	if output_file:
		write_output(output_file, output)
		print(f"Output writed at file {output_file}")
	else:
		sys.stdout.write(output)


if __name__ == "__main__":

	output_file = None
	if not len(sys.argv) > 1:
		print("Missing target file")
		exit(1)
	if len(sys.argv) > 2:
		output_file = sys.argv[2]

	filename = sys.argv[1]
	obfuscate(filename, output_file)
	#f = num_parser(sys.argv[3])
	#print(f)
	#print(sum(f))
