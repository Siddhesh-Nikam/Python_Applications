print("Start of Program")

s1=input("Enter some text:")
print("Entered text:",s1)
print("type(s1):",type(s1))

s2=input("Enter an integer:")
print("Entered integer:",s2)
print("type(s2):",type(s2))

s3=input("Enter fractional number:")
print("Entered fractional number:",s2)
print("type(s3):",type(s3))

n=int(s2)
print("n:",n)
print("type(n):",type(n))

f_num = float(s3)
print("f_num:",f_num)
print("type(f_num):",type(f_num))

print("int(s1) and float(s2) do not change string objects")
print("They simply return a new integer object and a new floating object")

print("type(s1):",type(s1))#<class 'str'>
print("type(s2):",type(s2))#<class 'str'>
print("type(s3):",type(s3))#<class 'str'>

print("type(n)",type(n))#<class 'int'>
print("type(f_num):",type(f_num))#<class 'float'>

print("End of Program")
 
