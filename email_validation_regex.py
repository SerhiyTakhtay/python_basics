import  re
pattern = re.compile (r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'abc@hotmail.com'
a = pattern.search(string)
 
if a :
  print('We have a match')
else:
  print ('Please search for a real email adreess only')
