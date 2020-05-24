#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, json, getopt, os

def usage():
	print 'Usage: addTranslatableStrings.py -i <inputPath> -o <outputPath>'
	
def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

def findAllIndexes(line, quote):
    start = 0
    while True:
        start = line.find(quote, start)
        if start == -1: return
        yield start
        start += len(quote) # use start += 1 to find overlapping matches

def addQuotes(line, checkComma):
	times = len(list(findAllIndexes(line, "\"")))/2
	for x in range(times):
		firstQuote = findnth(line, "\"", 0 + x * 2)
		line = line[:firstQuote] + "__(" + line[firstQuote:]
		secondQuote = findnth(line, "\"", 1 + x * 2) + 1
		line = line[:secondQuote] + ")" + line[secondQuote:]
	indexEndOfLine = len(line) - 1
	if checkComma and line.strip()[len(line.strip()) - 1] != ",":
		line = line[:indexEndOfLine] + "," + line[indexEndOfLine:]
	return line
	
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
	print "Adding translatable strings..."
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
				with open(inputPath + name, 'r') as file:
					randomChoice = False
					for line in file:
						if "renpy.random.choice([\"" in line:
							randomChoice = True
							if "]" in line:
								randomChoice = False
						elif "]" in line and randomChoice:
							line = addQuotes(line, False)
							randomChoice = False
						if randomChoice:
							line = addQuotes(line, True)
						if "$ Line = \"" in line and not "$ Line = \"\"" in line:
							index = line.index("$ Line = \"") + 9
							line = line[:index] + "__(" + line[index:]
							# if line is not inline
							indexNewLine = findnth(line, "$", 0)
							line = line[:indexNewLine] + line[indexNewLine:].strip()
							if line[len(line) - 1] != "\"":
								index2 = findnth(line, "\"", 1)
								line = line[:index2 + 1] + ")" + line[index2 + 1:] + "\n"
							else:
								line = line + ")\n"
						if "Line == \"" in line:
							indexLine = findnth(line, "Line ==", 0)
							line = line[:indexLine] + addQuotes(line[indexLine:], False)
						lines.append(line)
					with open(outputPath + name, 'wb') as f:
						for line in lines:
							f.write(line)
				print "Finished for" + inputPath + name + "."

if __name__ == "__main__":
    main(sys.argv[1:])
	
