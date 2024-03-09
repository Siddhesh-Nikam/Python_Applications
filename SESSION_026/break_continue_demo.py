# break_continue_demo.py
import sys

print("start of program") 
N = int(input("Enter desired number of elements in list:"))

if N <= 0:
    print("List must contain at least one element")
    sys.exit(-1)

L = []
i = 0
while i < N:
    L.append(int(input("Enter next value:")))
    i = i + 1 

print("Break demo") 
for x in L:
    print("start of iteration")
    if x % 7 == 0:
        break
    print(x)
    print("end of iteration") 

print("Continue demo") 
for x in L:
    print("start of iteration")
    if x % 7 == 0:
        continue
    print(x)
    print("end of iteration")
print("end of program")
