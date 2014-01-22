#!/usr/bin/python

import sys
import re
#version 2.1 making the file a parameter
def symbol_extractor (file):
	""" Usage, $ python symbol_extractor_v2_works.py your_file.txt     it returns a list of document symbols found in the given file.\n\
	Includes the function extract_symbol('string') which accepts a string instead of a file. """
	return extract_symbol(file_get_text (file))

def file_get_text (my_file):
	with open(my_file, 'r+') as f:
		string_to_analize = f.read()
	return string_to_analize

# required segments should be used for the 1st & 2nd segments of a symbol e.g. required/required
req_seg = r"""
	                    			\w+			#1st word required
	                    			\.*			#dot optional
	                    			-*			#- optional
		                    		\w*			#word after dot optional
	                    			\.*			#dot optional
	                    			-*			#- optional
	                    			\w*			#word after dot optional
	  	                    	"""
req_slash = r"""/"""
opt_slash = r"""/*"""
opt_seg = r"""
	                    			\w*			#1st word optional
	                    			\.*			#dot optional
	                    			-*			#- optional
		                    		\w*			#word after dot optional
	                    			\.*			#dot optional
	                    			-*			#- optional
	                    			\w*			#word after dot optional
	  	                    	"""

def extract_symbol (my_string):
	reg_ex = re.compile(req_seg + req_slash + req_seg + opt_slash + opt_seg + opt_slash + opt_seg + opt_slash + opt_seg + opt_slash + opt_seg + opt_slash + opt_seg + opt_slash + opt_seg , re.X) # verbose flag
	return re.findall(reg_ex, my_string)


#test all
print '\n These are the symbols found in the document'
b = symbol_extractor('test.txt')
#b = symbol_extractor(sys.argv[1])
#print b
print '<results>'
for item in b :
	print '    <item>' + item + '</item>'
print '</results>'


print('Content-type: text/html\n')
print('<TITLE>CGI 101</TITLE>')
print('<H1>A First CGI Script</H1>')
print(b)
