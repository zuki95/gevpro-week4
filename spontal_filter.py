#!/usr/bin/env python
#spontan_filter.py

import sys

def main():
	import xml.etree.ElementTree as ET
	tree = ET.parse('spontal.xml')
	root = tree.getroot()

	for data in root.findall('spontal'):
		
		BOTTOM_HZ = int(data.find('BOTTOM_HZ').text)
		TOP_HZ = int(data.find('TOP_HZ').text)
		F0_START = int(data.find('F0_START').text)
		F0_END = int(data.find('F0_END').text)
		if F0_START < BOTTOM_HZ:
			root.remove(data)
		elif F0_END > TOP_HZ:
			root.remove(data)
		else:
			tree.write('spontal_filtered.xml')
			
			
#def main(argv):
	
	#if len(sys.argv) == 4:
		#continue
		
	#else:
		#print("Usage: $ python Arg1, Arg2, Arg3", file=sys.stderr)
		
		
if __name__ == "__main__":
		main()
		
	
			
			
			
		
	

