# At least 8 character long
# It has numbers letters and a special symbol
# has to end with a number 
import re
pattern = re.compile (r"[a-zA-Z0-9]{8,}[^a-zA-Z0-9_]+\d+$")
password = input('Please enter your password minimum 8 caracters with low or upper case latter, must have a special symbol and the last carracter need to be a number ')
check = pattern.fullmatch(password)
if check:
	print('You have valid password')
else:
	print('You password is not valid')

