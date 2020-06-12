#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, json, getopt

class Translatable:
	id = 0
	ref = ""
	fuzzy = ""
	msgctxt = ""
	msgid = ""
	msgstr = ""

def usage():
	print 'Usage: unfuzzyDuplicates.py -i <inputFile> -o <outputFile> [-v]'
	
def main(argv):
	try:
		opts, args = getopt.getopt(argv, "i:o:v")
		if len(sys.argv) < 4:
			usage()
			sys.exit(2)
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	verbose = False
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
		elif opt in ("-i"):
			inputFile = arg 
		elif opt in ("-v"):
			verbose = True
		elif opt in ("-o"):
			outputFile = arg
	print "Stocking translatables..."
	counter = 0
	translatables = []
	lastTranslatable = {}
	storeMsgId = False
	storeMsgStr = False
	with open(inputFile, 'r') as poFile:
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
		print "Translatables stored, detecting the ones that need to be unfuzzied..."
		unfuzzyTranslations = {}
		alreadyParsedMsgIds = []
		# Storing unfuzzy (validated) msgid and msgstr
		for trans in translatables:
			if trans.fuzzy == "" and trans.msgstr != "" and trans.msgid not in alreadyParsedMsgIds:
				unfuzzyTranslations[trans.msgid] = trans.msgstr
				alreadyParsedMsgIds.append(trans.msgid)
		print "Writing new files in unix format..."
		with open(outputFile, 'wb') as f:
			for trans in translatables:
				f.write("\n")
				f.write(trans.ref)
				# Write fuzzy line only if msgid was parsed earlier
				if trans.fuzzy != "" and not trans.msgid in alreadyParsedMsgIds:
					f.write(trans.fuzzy)
				if trans.fuzzy != "" and trans.msgid in alreadyParsedMsgIds and verbose:
					print trans.msgid.strip() + " unfuzzied."
				if trans.msgctxt != "":
					f.write(trans.msgctxt)
				f.write(trans.msgid)
				# Writing translation stored in unfuzzy array if available
				if trans.msgid in alreadyParsedMsgIds:
					f.write(unfuzzyTranslations[trans.msgid])
					if verbose and trans.fuzzy != "" and trans.msgstr != unfuzzyTranslations[trans.msgid]:
						print trans.msgstr + "replaced by: " + unfuzzyTranslations[trans.msgid].strip()
				else:
					f.write(trans.msgstr)
	print "Finished."

if __name__ == "__main__":
    main(sys.argv[1:])
	
