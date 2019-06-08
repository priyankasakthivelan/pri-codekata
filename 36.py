import re
para=input()
specialchars = len(para) - len( re.findall('[\w]', para) )
print(specialchars)