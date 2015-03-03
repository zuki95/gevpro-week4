#!/usr/bin/python3
#Kamil Zukowski
#blood.py

import sys
import json
from collections import namedtuple

def main():
	#Opens json file, creates an empty list and defines the namedtuple
	in_file = json.load(open("blood-die.json"))
	list_match = []
	matches = namedtuple('matches', 'language, classifications')
	
	for language in in_file:
		name = language[0]
		_class = language[1]
		word_blood = language[2]
		word_die = language[3]
		
		list_blood = word_blood.strip().split(", ")
		list_die = word_die.strip().split(", ")
	#Finds matches of words and appends them	
		for word_blood in list_blood:
			for word_die in list_die:
				if(word_blood == word_die):
					list_match.append(matches(name, _class))
	#Prints the result using a list comprehension				
	print([language for (language, classifications) in list_match])
	
if __name__ == "__main__":
	main()
					
