#Program to reverse a given Number.    ex: n=123   Reversed no is 321

num = int(input())
rev = 0
while num > 0:
  rem = num % 10  
  rev = (rev*10) + rem
  num = num//10  
print(rev)
