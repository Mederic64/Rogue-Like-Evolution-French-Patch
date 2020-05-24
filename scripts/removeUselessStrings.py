#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, json, getopt, os

class Line:
	useless = False
	value = ""
	index = 0

def usage():
	print 'Usage: removeUselessStrings.py -i <inputPath> -o <outputPath>'
	
def main(argv):
	try:
		opts, args = getopt.getopt(argv, "i:o:")
		if len(sys.argv) < 4:
			usage()
			sys.exit(2)
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
		elif opt in ("-i"):
			inputPath = arg 
		elif opt in ("-o"):
			outputPath = arg
	print "Removing useless strings..."
	for root, dirs, files in os.walk(inputPath, topdown=False):
		for name in files:
			if name[-4:][:1] == '.':
				extension = name[-3:]
			else:
				if name[-5:][:1] == '.':
					extension = name[-4:]
				else:
					break
			if extension == 'rpy':	
				lines = []
				counter = 0
				with open(inputPath + name, 'r') as file:
					for line in file:
						newLine = Line()
						newLine.index = counter
						newLine.value = line
						if "Project-Id" in line:
							newLine.useless = True
							for x in range(5):
								x = x + 1
								lines[newLine.index - x].useless = True
						lines.append(newLine)
						counter = counter + 1
					with open(outputPath + name, 'wb') as f:
						for line in lines:
							if not line.useless:
								f.write(line.value)
				print "Finished for" + inputPath + name + "."

if __name__ == "__main__":
    main(sys.argv[1:])
	
