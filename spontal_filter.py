#!/usr/bin/python3
#Kamil Zukowski, 25-02-2015
#spontal_filter.py

import sys

def main(argv):
	
	source = argv[1]
	destination = argv[2]
	
	import xml.etree.ElementTree as ET
	tree = ET.parse(source)
	root = tree.getroot()

	for POINT in root.findall('POINT'):
		
		BOTTOM_HZ = float(POINT.find('BOTTOM_HZ').text)
		TOP_HZ = float(POINT.find('TOP_HZ').text)
		F0_START = float(POINT.find('F0_START').text)
		F0_END = float(POINT.find('F0_END').text)
		
		if((F0_START < BOTTOM_HZ) or (F0_START > TOP_HZ) or (F0_END < BOTTOM_HZ) or (F0_END > TOP_HZ)): 
			root.remove(POINT)
	
	tree.write(destination)
			
			
if __name__ == "__main__":
		main(sys.argv)
		
	
			
			
			
		
	

