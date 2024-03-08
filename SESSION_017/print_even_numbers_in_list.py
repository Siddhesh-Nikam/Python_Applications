import sys

strN = input("Enter the length of the list:")
N = int(strN)

if N<0:
    print("Length of string must be positive")
    sys.exit()

L = []

i = 0

while i<N:
    s = input("Enter an element:")
    num=int(s)
    L.append(num)
    i = i + 1

print("Printing all even numbers in the list")

i = 0 
while i<N:
    if L[i] % 2 == 0:
        print(L[i])
    i = i + 1