#Program to find digital sum of a given Number

n=int(input("Enter a number:"))
s=0
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
print("The total sum of digits is:",s)

