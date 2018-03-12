'''
Created on 12 Mar 2018

@author: amar.prasovic
'''
S = 'The quick brown fox jumps over the lazy dog'
print(dir(S))

print(S.count('p'))

print(S + 'NI')

print(S.__add__('NI'))

print(help(S.replace))

print(S.replace('l', 'L'))

help(str)

print(help())

P = 'A\nB\tC'
print(len(P))

print(P)

print(ord('\n'))

R = 'A\0B\0C'
print(len(R))
print(R)

print('sp' + '\xc4' + '\u00c4' + '\U000000c4' + 'm')









