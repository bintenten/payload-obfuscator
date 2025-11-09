import sys
import random
import base64
import argparse

sys.set_int_max_str_digits(10000000)

def concat(first, last):
	calc = f'((' + first + ') + ' + last + ')'
	return calc

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

	decimals_info = {"formulas":[], "numbers":[], "lengths":[]}
	for char in text:
		number = ord(char)
		parsed_num = num_parser(number)
		length_num = len(str(number))
		number_formula = ' + '.join([str(num) for num in parsed_num])

		size_plus_number_formula = f"(({length_num} * 10 ** {length_num}) + ({number_formula}))"
		calculated_number = eval(size_plus_number_formula)
		decimals_info["formulas"].append(size_plus_number_formula)
		decimals_info["numbers"].append(calculated_number)
		decimals_info["lengths"].append(length_num + 1)

	full_number = 0
	len_numbers = len(decimals_info["numbers"])
	full_formula = ''
	for index in range(len_numbers):
		zeros_right = sum(decimals_info["lengths"][index+1:])
		zeros_right_parsed = '(10 ** (' + (' + '.join([str(num) for num in num_parser(zeros_right)]) if zeros_right else '0') + ') * ' + str(decimals_info["formulas"][index])  + ')'
		if index + 1 != len_numbers:
			full_formula += zeros_right_parsed + ' + '
		else:
			full_formula += zeros_right_parsed
		pot = 10 ** zeros_right
		partial_number = pot * decimals_info["numbers"][index]
		full_number += partial_number

	if output_file:
		write_output(output_file, full_formula)
		print(f"Output writed at file {output_file}")
	else:
		sys.stdout.write(full_formula)
		pass

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

	obfuscate(filename, output_file, encode_base64)
