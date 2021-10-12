# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {3: 'box', 1: 'choclate'}

# dictionary with mixed keys
my_dict = {'name': 'Ahimsa', 1: [2, 4, 3]}

# using dict()
my_dict = dict({3:'box', 1:'choclate'})

# from sequence having each item as a pair
my_dict = dict([(3,'box'), (1,'choclate')])


#Accessing Elements from Dictionary

# get vs [] for retrieving elements
my_dict = {'name': 'Rohan', 'age': 20}

# Output: Jack
print(my_dict['name'])

# Output: 20
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))

# KeyError
print(my_dict['address'])


#Changing and Adding Dictionary elements

# Changing and adding Dictionary Elements
my_dict = {'name': 'Rohan', 'age': 20}

# update value
my_dict['age'] = 26

#Output: {'age': 26, 'name': 'Rohan'}
print(my_dict)

# add item
my_dict['address'] = 'Bombay'

# Output: {'address': 'Bombay', 'age': 26, 'name': 'Rohan'}
print(my_dict)


#Removing elements from Dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item, return (key,value)
# Output: (5, 25)
print(squares.popitem())

# Output: {1: 1, 2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
print(squares)


# Iterating through a Dictionary

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])


#Dictionary Methods

# keys() methods
food = {'Tom': 'Burger', 'Jim': 'Pizza', 'Tim': 'Fries'}
f = food.keys()
print(f)

#dictionary values()
food = {'Tom': 'Burger', 'Jim': 'Pizza', 'Tim': 'Fries'}
f = food.values()
print(f)

#dictionary get() 
employee = {1020: 'Kim', 1021: 'Ani', 1022: 'Mishka'}
print(employee.get(1021))

# add() item method
employee = {1020: 'Kim', 1021: 'Ani', 1022: 'Mishka'}
employee[1023] = 'Tom'
print(employee)

#dictionary len() 
employee = {1020: 'Kim', 1021: 'Ani', 1022: 'Mishka'}
print(len(employee))


#dictionary list 

dict = {}
dict["Name"] = ["Jack"]
dict["Marks"] = [45]
print(dict)