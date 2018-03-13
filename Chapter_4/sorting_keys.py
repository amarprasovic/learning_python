'''
Created on 13 Mar 2018

@author: amar.prasovic
'''
X = {'a':1, 'c':3, 'b':2}
print(X)

Ks = list(X.keys())
print(Ks)

Ks.sort()

for key in Ks:
    print(key, '=>', X[key])
    
for key in sorted(X):
    print(key, '=>', X[key])
    
for c in 'spam':
    print(c.upper())
    
x = 4
while x > 0:
    print('spam!' * x)
    x -= 1
    
squares = [x ** 2 for x in [1, 2, 3, 4]]

print(squares)

squares1 = []
for x in [1, 2, 3, 4, 5]:
    squares1.append(x ** 2)

print(squares1)