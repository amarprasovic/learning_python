'''
Created on 12 Mar 2018

@author: amar.prasovic
'''
S = 'Spam'

print(len(S))   #print the length of the string saved in variable S
print(S[0])     #print the first item in S
print(S[1])     #print the second item in S

print(S[-1])
print(S[-3])

print(S[-1])
print(S[len(S)-1])

print(S[1:3])

print(S[1:])
print(S[0:3])
print(S[:3])
print(S[:-1])
print(S[:])

print(S + 'xyz')

print(S * 8)

print(S)

#print(S[0] = 'z')

S = 'z' + S[1:]
print(S)

S = 'S' + S[1:]

P = 'shrubbery'
L = list(P)
print(L)

L[1] = 'c'
print(''.join(L))

B = bytearray(b'spam')
B.extend(b'eggs')
print(B)

print(B.decode())