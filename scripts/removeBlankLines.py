#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, json, getopt, os

class Translatable:
	id = 0
	ref = ""
	fuzzy = ""
	msgctxt = ""
	msgid = ""
	msgstr = ""

def usage():
	print 'Usage: removeBlankLines.py -i <inputPath> -o <outputPath>'
	
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
	print "Stocking translatables..."
	counter = 0
	translatables = []
	lastTranslatable = {}
	storeMsgId = False
	storeMsgStr = False
	with open(inputPath, 'r') as poFile:
		for line in poFile:
			# Newline means new translatable
			if line == "\n":
				if 'newTranslatable' in locals():
					translatables.append(newTranslatable)
				# New translatable means no more msgstr for previous one
				storeMsgStr = False
				newTranslatable = Translatable()
				# setting translatable ID
				newTranslatable.id = counter
			# Storing translatable reference
			if line[:2] == "#:":
				if not 'newTranslatable' in locals():
					storeMsgStr = False
					newTranslatable = Translatable()
					newTranslatable.id = counter
				newTranslatable.ref = line
			# Detecting if translatable is fuzzy
			if line[:2] == "#,":
				newTranslatable.fuzzy = line
			# Storing translatable msgctxt
			if line[:7] == "msgctxt":
				newTranslatable.msgctxt = line
			# Storing translatable original text and translated text, inline or not
			if line[:5] == "msgid" and 'newTranslatable' in locals():
				if len(line) == 9:
					storeMsgId = True
				else:
					newTranslatable.msgid = line
			if line[:6] == "msgstr" and 'newTranslatable' in locals():
				storeMsgId = False
				if len(line) == 10:
					storeMsgStr = True
				else:
					newTranslatable.msgstr = line
			if storeMsgId == True:
				newTranslatable.msgid = newTranslatable.msgid + line
			if storeMsgStr == True:
				newTranslatable.msgstr = newTranslatable.msgstr + line
			if 'newTranslatable' in locals():
				lastTranslatable = newTranslatable
			counter = counter + 1
		translatables.append(lastTranslatable)
	print "Translatables stored, removing blank lines..."
	# Storing unfuzzy (validated) msgid and msgstr
	for trans in translatables:
		if trans.msgid == "msgid \"\"\n":
			translatables.remove(trans)
	print "Writing new files in unix format..."
	with open(outputPath, 'wb') as f:
		for trans in translatables:
			f.write(trans.ref)
			if trans.fuzzy != "":
				f.write(trans.fuzzy)
			if trans.msgctxt != "":
				f.write(trans.msgctxt)
			f.write(trans.msgid)
			f.write(trans.msgstr)
			if trans != translatables[len(translatables) - 1]:
				f.write("\n")
		
	print "Finished."

if __name__ == "__main__":
    main(sys.argv[1:])
	
