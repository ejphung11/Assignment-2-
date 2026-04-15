
import argparse
import random
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--echo', action='store_true', help='treat each ARG as an input line')
parser.add_argument('-i', '--input-range', metavar='LO-HI', help='treat each number LO through HI as an input line')
parser.add_argument('-n', '--head-count', type=int, metavar='COUNT', help='output at most COUNT lines')
parser.add_argument('-r', '--repeat', action='store_true',help='output lines can be repeated')
parser.add_argument('input', nargs='*', help='input file or input lines with -e')


args = parser.parse_args()

def parse_input_range(range_str):
	parts = range_str.split('-')

	if len(parts) != 2:
		raise ValueError("Invalid Input Range")

	try:
		lo = int(parts[0])
		hi = int(parts[1])
	except ValueError:
		raise ValueError("Invalid Input Range")
	if lo > hi:
		raise ValueError("Invalid Input Range")
	return lo, hi

def read_input_lines(inputs):
	if len(inputs) == 0:
		return sys.stdin.read().splitlines()

	if len(inputs) == 1:
		if inputs[0] == '-':
			return sys.stdin.read().splitlines()

		try:
			with open(inputs[0], 'r') as f:
				return f.read().splitlines()
		except OSError as e:
			sys.exit("shuf.py: " + str(e))

	sys.exit("shuf.py: extra operand")


if args.head_count is not None and args.head_count < 0:
	parser.error("negative count")

if args.echo and args.input_range:
	parser.error("cannot combine -e and -i")


if args.echo:
	lines = args.input

elif args.input_range:
	if len(args.input) != 0:
		parser.error("extra operand " + args.input[0])
	try:
		lo,hi = parse_input_range(args.input_range)
	except ValueError as e:
		parser.error(str(e))

	lines = []
	for i in range(lo, hi + 1):
		lines.append(str(i))


else:
	lines = read_input_lines(args.input)

if args.repeat:
	if len(lines) == 0:
		sys.exit("shuf.py: no lines repeat")

	if args.head_count is None:
		while True:
			print(random.choice(lines))

	else:
		for i in range(args.head_count):
			print(random.choice(lines))
else:
	random.shuffle(lines)

	if args.head_count is None:
		for line in lines:
			print(line)

	else:
		for line in lines[:args.head_count]:
			print(line)












