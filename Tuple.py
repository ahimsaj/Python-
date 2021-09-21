#tuples 

Tuple = (2,3,4)
print(Tuple)

#Empty tuple

tuple = ()
print(tuple)

#Types of tuples 

Boolean = (True,False)
IntTuple = (1,2,3,4,5,)
FloatTuple = (1.1,1.2,1.3,1.4,1.5)
StringTuple = ("u","v","w","x","y","z")

print(Boolean)
print(IntTuple)
print(FloatTuple)
print(StringTuple)

#tuple with mixed datatypes

tuple1 = (1, "Hello", 9.2)
print(tuple1)

#Nesting of tuples 

tuple1 = (1,2,3)
tuple2 = ("Ahimsa","04")
tuple3 = (tuple1, tuple2)

print(tuple3)

#tuple unpacking 
tuple1 = "ahimsa", 0.4, "jain"

print(tuple1)

a, b, c = tuple1

print(a)    
print(c)    
print(b)    

#Accessing tuple elements using indexing
tuple1 = ('1','2','3','4','5','6')

print(tuple1[3])   
print(tuple1[5])  

#Accessing tuple elements using slicing
tuple1 = ('p','r','o','g','r','a','m','i','z')

# elements 1nd to 4th
print(tuple[1:4])

# elements beginning to 2nd
print(tuple1[:-7])

# elements 8th to end
print(tuple1[7:])

# elements beginning to end
print(tuple1[:])

#Functions on tuples 

tuple1 = (11,21,31,41,51,61,71,81,91)
maximum = max(tuple1)
minimum = min(tuple1)

print("Max: ", maximum)
print("Min: ",minimum)

print("Len: ", len(tuple1))

# Concatenation
print((10, 20, 30) + (40, 50, 60))

# Repeat
print(("Python",) * 5)

# Membership test in tuple
tuple1 = ('a', 'z', 'b', 'y')

# In operation
print('a' in tuple1)
print('p' in tuple1)

# Not in operation
print('g' not in tuple1)

# Using a for loop to iterate through a tuple
for name in ('Ahimsa' ,'Jain'):
    print("Myself", name)

#deleting a tuple

tuple1 = (22,33,44,55,66,77)

print(tuple1)
del tuple1
print(tuple1)





