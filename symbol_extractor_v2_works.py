import re
#version 2 is working fine
def symbol_extractor (file):
	""" Usage, >>> symbol_extractor('yourfile.txt') it returns a list of document symbols found in the given file.\n\
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

#test only extract_symbol function
text = r'hola amigos resolution sc-res-ece/123 hola a/64/567 resolution 67/5, and 45.25 56.67.5  E.esc.a/ESCAP.8/info.67/iop/5/6/7.items.long  ESCAP/967/27.Add.1_eng resolution 234 E/ESCAP/info-67.9 . note:  new symbols have up to 7 segments with forward slash / and . and - within each segment. unstructured wording can be resolution s-15/1-2-3-4.9-abc.add.7/4.67-corrig-4.7--.eng, resolution 17/17. (notice the trailing . and ,) journal no.2013/18  note  '
a = extract_symbol(text)
print 'Test only extract_symbol function'
print a
print 'Pretty print'
for item in a :
	print item
	
#test all
print '\n Test the full symbol_extractor function on test.txt file'
b = symbol_extractor('test.txt')
print b