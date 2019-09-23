import sys

from parser import parser

if (len(sys.argv) != 2):
	print("Bad args number")
	sys.exit()
parser(sys.argv[1])
