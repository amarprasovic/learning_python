'''
Created on 13 Mar 2018

@author: amar.prasovic
'''
rec = {'name':{'first': 'Bob', 'last': 'Smith'}, 
'jobs': ['dev','mgr'],
'age': 40.5}

print(rec)

print(rec['name'])

print(rec['name']['last'])

print(rec['jobs'])

print(rec['jobs'][1])

rec['jobs'].append('janitor')

rec = 0

Z = {'a':1, 'b':2, 'c':3}

print(Z)

Z['e'] = 99

print(Z['f'])

#'f' in Z

if not 'f' in Z:
    print('missing')
    print('no, really...')
    
value = Z.get('x',0)

print(value)

value1 = Z['x'] if 'x' in Z else 0

print(value1)

