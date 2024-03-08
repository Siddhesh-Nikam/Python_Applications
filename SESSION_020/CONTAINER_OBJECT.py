s="ABC"
T= (100,200,300,400)
L=[True,100,1.1,3.8,False]
D={'a':1.1,'b':3.8,3.11:8080}

print(type(s))
print(type(T))
print(type(L))
print(type(D))

print(T[0])
print(T[1])
print(T[2])
print(T[3])

print(s[0])
print(s[1])
print(s[2])

print(D['a'])
print(D['b'])
print(D[3.11])

for x in D.keys():
    print(x, D[x])






