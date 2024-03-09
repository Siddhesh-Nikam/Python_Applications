import sys

N=int(input("Enter a positive integer:"))

if N<=1:
    print("Prime number testing can be done for int's >1 ")
    sys.exit(-1)

k=2
while k<=N//2:
    if N%k==0:
        print(N, " is not a prime number")
        break
    k=k+1

if k == (N//2)+1:
    print(N, " is a prime number")




