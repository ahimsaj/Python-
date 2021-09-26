#defining class

class First:
    pass
class intro:
    age=20
    def greet(self):
        print("hello")
obj=intro()
print(obj.age)
obj.greet()

##

class Class1:
  x = 5
p1 = Class1()
print(p1.x)

##

class Me:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Me("Ahimsa", 19)
p1.myfunc()

#stack

class Stack:
  def __init__(self):
    self.stack = []
  def add(self, dataval):
    if dataval not in self.stack:
      self.stack.append(dataval)
      return True
    else:
      return False
  def peek(self):
    return self.stack[-1]
AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())



