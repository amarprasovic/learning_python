'''
Created on 13 Mar 2018

@author: amar.prasovic
'''
import struct

f = open('git/learning_python/Chapter_4/data.txt','w')

f.write('Hello\n')
f.write('world\n')
f.close()

print(f)

f = open('git/learning_python/Chapter_4/data.txt','r')
text = f.read()

print(text)

for line in open('git/learning_python/Chapter_4/data.txt'):
    print(line)
    
dir(f)

help(f.seek)

packed = struct.pack('>i4sh', 7, b'spam', 8)

print(packed)

file = open('git/learning_python/Chapter_4/data.bin','wb')
file.write(packed)
file.close()

data = open('git/learning_python/Chapter_4/data.bin','rb').read()

print(data)

print(data[4:8])

print(list(data))

print(struct.unpack('>i4sh', data))
