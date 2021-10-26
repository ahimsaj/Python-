#To check whether a number is divisible by 8 and 12 or not.
a=int(input("enter a number"))
b=a%8 and a%12
if b==0:
    print("divisible")
else:
    print("not divisible")
