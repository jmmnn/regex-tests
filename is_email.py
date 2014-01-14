def find_email (list):
	"""This function extracts e-mail addresses from a list\n\
	The given list must include only strings\n\
	 e.g. >>> my_list = ['123@er.com', 'not-an-email.com', '6789'] \n\
	 >>> find_email(my_list)\n\
	 ['123@er.com']
	 """
	
	#this removes the white spaces from each item on the list
	# using the str.strip built-in method
	list = map(str.strip, list)
	#this checks if each item is an email adress
	return filter(is_email, list)

def is_email (x) :
	"""This function check if the argument is an e-mail addresses\n\
	The argument must be a string\n\
	 """
	if x.count('@') == 1:
		return True 
	else:
		return False

#function is_email_allowed to check whether a string 'rule' e.g. username or domain is allowed
# not implemented
	
#test is_e_mail allowed
def test_is_email_allowed():
	my_rule = 'toto'
	my_email = 'pepito@toto.com'
	my_email2 = 'pepito@pato.com'
	return is_email_allowed(my_email, my_rule), is_email_allowed(my_email2, my_rule)

	
#test the whole
def test_email () :
	my_list = ['123@er.com.      ', '        an-@email.com', '6789@3@9', '9090', '123@toto.com']
	my_unwanted_domains = 'toto'
	return find_email(my_list)


