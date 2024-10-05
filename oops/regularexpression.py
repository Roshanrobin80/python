'''import re
a='welcome to jumanji'
#print(re.sub('to','To',a))
#print(re.sub('too','To',a))
#print(re.split('',a))
#print(re.findall('to',a))
#print(re.findall('tot',a))
a='welcome to all to to to'
#print(re.findall('to',a))
#print(re.search('to',a))
a='abcd'
#print(re.search('a',a))
#print(re.search('a.',a))
#print(re.search('d.',a))
#print(re.search('d.*',a))
#print(re.search('a.*',a))
#print(re.search('d.+',a))
#print(re.search('c.+',a))
#print(re.search('c.?',a))
#print(re.search('d.?',a))
#print(re.search('a.?',a))
#print(re.search('[a-z]',a))
#print(re.search('[A-Z]',a))
# a='ASDF'
#print(re.search('[A-Z]',a))
#print(re.search('[A-I]',a))
#print(re.search('[M-Z]',a))
a='99437'
#print(re.search('[0-9]',a))
#print(re.search('[6-9]',a))
a='abc123'
#print(re.search('[a-z][0-9]',a))
#print(re.search('[a-z0-9]',a))
a='2345'
#print(re.search('[a-z][0-9]',a))
a='abcd'
#print(re.search('[abcd]',a))
#print(re.search('[a-z].',a))
#print(re.search('[a-z].*',a))
#print(re.search('[a-z].+',a))
#print(re.search('[a-z].?',a))
#print(re.search('[a-z].*[0-9]',a))
a='abcd9'
#print(re.search('[a-z].*[0-9]',a))
a='abcd789'
#print(re.search('[a-z].*[0-9]',a))
#print(re.search('[a-z].{3}',a))
a='abcd'
#print(re.search('[a-z].{3}',a))
#print(re.search('[a-z].{4}',a))'''

#programs

#ph.no validation

'''import re
a='7306854116'
if len(a)==10 and re.search('[6-9].{9}',a) and a.isdigit():
    print('ph.no is valid')
else:
    print('no. not valid')'''

#email validation

import re
'''a=str(input('enter email: '))
if re.search('^[a-z].*@gmail.com$',a):
    print('email is valid')
else:
    print('not valid')'''

#password validation
a=str(input('enter password: '))
if re.search('^[A-z].*[@#$&.0-9]',a) and not(a.isdigit()) and len(a)>=8:
    print('password is valid')
else:
    print('password not valid')



