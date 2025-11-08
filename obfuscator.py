import sys
import random
import base64
import argparse

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


def obfuscate(filename, output_file, encode_base64):
	text = read_file(filename)
	if not text:
		print(f"File {filename} is empty")
		exit(1)

	if encode_base64:
		byte_text = text.encode("utf-8")
		text = base64.b64encode(byte_text).decode("utf-8")
		print(text)

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

	parser = argparse.ArgumentParser(prog="MABfuscator", description="File obfusction through Ascii Algoritm")

	parser.add_argument("-o", "--output", help="Obfuscation output file")
	parser.add_argument("-f", "--file", help="File to obfuscate")
	parser.add_argument("-b64", "--base64", action="store_true", help="Encode the file content to base64 before obfuscate")

	args = parser.parse_args()

	filename = args.file
	if not filename:
		print("Please enter the file to obfuscate")
		exit(1)

	output_file = args.output
	encode_base64 = args.base64
	print(filename, output_file, encode_base64)

	obfuscate(filename, output_file, encode_base64)

