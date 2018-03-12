'''
Created on 12 Mar 2018

@author: amar.prasovic
'''

S = 'Spam'

S.find('pa')

print(S)

S.replace('pa', 'XYZ')

print(S)

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))

print(line)

print(S.upper())

print(S.isalpha())

print(S.isdigit())

line2 = 'aaa,bbb,ccccc,dd\n'

print(line2)

print(line.rstrip())

print(line.rstrip().split(','))

print('%s, eggs, and %s' %('spam', 'SPAM'))         #Substitution C-like

print('{}, eggs and {}'.format('spam', 'SPAM'))     #Substitution new from 2.7, 3.0

print('{0}, eggs and {1}'.format('spam', 'SPAM'))   #Substitution old (works with 3.6)

