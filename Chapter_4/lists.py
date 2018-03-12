'''
Created on 12 Mar 2018

@author: amar.prasovic
'''
L = [123, 'spam', 1.23]

print(len(L))
      
print(L[0])

print(L[:-1])

print(L + [4, 5, 6])

print(L * 2)

print(L)

L.append('NI')
print(L)

print(L[2])

L.pop(2)
print(L)

M = ['bb', 'aa', 'cc']

M.sort()

print(M)

M.reverse()

N = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(N)

print(N[1][1])


row2 = N[1]

col2 = [row[1] for row in N]

print(row2)

print(col2)

print([row[1]+5 for row in N])

print([row[1] for row in N if row[1] % 2 == 0])

diag = [N[i][i] for i in [0,1,2]]

print(diag)

doubles = [c * 2 for c in 'spam']
print(doubles)
print(''.join(doubles))

print(list(range(4)))

print(list(range(-6, 7, 2)))

print([[x, x ** 2, x ** 3] for x in range(4)])

print([[x, x /2, x *2] for x in range(-6, 7, 2) if x > 0])

G = (sum(row) for row in N)

print(next(G))
