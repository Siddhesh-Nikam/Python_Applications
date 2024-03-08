import sys

strN = input("Enter the length of the list:")
N = int(strN)

if N<=0:
    print("Length of the list must be positive ")
    sys.exit()

L = []

i=0

while i<N:
    s=input("Enter an element:")
    num=int(s)
    L.append(num)
    i = i + 1


print("List of length and element of your choice:",L)
sys.exit()