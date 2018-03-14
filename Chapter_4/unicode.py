'''
Created on 13 Mar 2018

@author: amar.prasovic
'''

S = 'sp\xc4m'
print(S)

print(S[2])

file = open('git/learning_python/Chapter_4/unidata.txt','w',encoding='utf-8')

file.write(S)

file.close()

text = open('git/learning_python/Chapter_4/unidata.txt',encoding='utf-8').read()

print(text)

len(text)

raw = open('git/learning_python/Chapter_4/unidata.txt','rb').read()

print(raw)

text.encode('utf-8')

raw.decode('utf-8')

text.encode('utf-16')
text.encode('latin-1')

print(len(text.encode('latin-1')), len(text.encode('utf-16')))