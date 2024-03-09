L = [3,5,6,12,78,43]

print("while loop:")
i=0
while i<len(L):
    if L[i]%2==0:
        print(L[i])
    i=i+1


print("for loop:")

for x in L:
    if x%2 == 0 :
        print(x)
    
