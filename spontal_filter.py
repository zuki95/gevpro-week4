#!/usr/bin/python3
#Kamil Zukowski, 25-02-2015
#spontal_filter.py

import sys
import xml.etree.ElementTree as ET

def main(argv):
	#Input file is argv[1] and destination file is argv[2]
	source = argv[1]
	destination = argv[2]
	
	tree = ET.parse(source)
	root = tree.getroot()
    #Iterates over the points in the corpus of the file
	for POINT in root:
		
		BOTTOM_HZ = float(POINT.find('BOTTOM_HZ').text)
		TOP_HZ = float(POINT.find('TOP_HZ').text)
		F0_START = float(POINT.find('F0_START').text)
		F0_END = float(POINT.find('F0_END').text)
	#Checks whether values of F0_START and F0_END are between the limits of HZ		
		if((F0_START < BOTTOM_HZ) or (F0_START > TOP_HZ) or (F0_END < BOTTOM_HZ) or (F0_END > TOP_HZ)): 
			root.remove(POINT)
	#Writes correct data to output
	tree.write(destination)
			
			
if __name__ == "__main__":
		main(sys.argv)
		
	
			
			
			
		
	

