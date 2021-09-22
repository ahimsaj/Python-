#use of function in python

def greet(name):
     print("Hello, " + name + ". Good morning!")

greet('Ahimsa')

#function with arguments

def evenOdd(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")

evenOdd(2)
evenOdd(3)


#passing list as an argument

def list1(open):
    for i in open:
        print(i)

list=[34,67,55,409]
list1(list) 

#Recursive function

def marks(k):
  if(k > 0):
    result = k + marks(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Results")
marks(6)

#global variable

x = "global"
def food():
    print("x inside:", x)

food()
print("x outside:", x)

#local variable

def food():
    y = "local"
    print(y)

food()

#Global variable and Local variable with same name

x = 5
def food():
    x = 10
    print("local x:", x)

food()
print("global x:", x)