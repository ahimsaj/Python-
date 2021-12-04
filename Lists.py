#list of integers

list = [2, 4, 8]

#list with mixed data types

list = [1, "Hello", 7]

#nested list

list = ["car", [1, 2, 3], ['p']]

#List indexing

list = ['a','h','i','m','s','a']

print(list[2])  
print(list[3])  

#Nested List

n_list = ["Ahimsa", [1, 0, 5, 9]]
#Nested indexing

print(n_list[0][1])
print(n_list[1][3])

#Addition of elements in a List

#Creating a List
List = [1,2,3]

print("Initial List: ")
print(List)

# Addition of Element at specific Position
List.insert(3, 12)
List.insert(0, 'alfa')

print("\nList after performing Insert Operation: ")
print(List)

#List slicing
list = ['a','b','c','d','e','f','g','h','i']

#excludes element at index 6
print(list[2:6])

#elements beginning to 5th
print(list[:-6])

#elements 6th to end
print(list[5:])

#elements beginning to end
print(list[:])

# Appending lists
word = [1, 3, 9]
word.append(2)

print(word)

#Deleting list items
list = ['t', 'u', 'v', 'w', 'x', 'y', 'z']

#delete one item
del list[1]
print(list)

#delete entire list
del list

#Sorting
colors = ['lavender', 'red', 'black']
colors.sort()
print(colors)

#Pop
colors = ['black', 'lavender', 'red']
colors.pop(1)
print(colors)

# Concatenating and repeating lists
start= [7, 8, 9]
print(start+[1, 2, 3])
print(["pro"] * 4)

#Reverse
colors = ['lavender', 'black', 'red']
colors.reverse()
print(colors)
