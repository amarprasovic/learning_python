'''
Created on 13 Mar 2018

@author: amar.prasovic
'''

D = {'food': 'Spam', 'quantity': 4, 'colour': 'pink'}

print(D)

print(D['food'])

D['quantity'] += 1 

C = {}

C['name'] = 'Bob'
C['job'] = 'developer'
C['age'] = 40

print(C)

print(C['name'])

bob1 = dict(name='Bob', job='developer', age=40)

print(bob1)

bob2 = dict(zip(['name','job','age'],['Bob','developer',40]))

print(bob2)