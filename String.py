#strings in Python

string1 = 'Hello'
print(string1)

string1 = "Hello"
print(string1)

string1 = '''Hello'''
print(string1)

# Python String Operations

str1 = 'Heyy'
str2 ='There!'

# using +

print('str1 + str2 = ', str1 + str2)

# using*

print('str1 * 3 =', str1 * 3)

# using triple quotes

print('''Myself, "Ahimsa Jain"''')

# escaping single quotes

print('Myself, "Ahimsa Jain"')

# escaping double quotes

print("Myself, Ahimsa Jain")

#Looping 

for x in "Success":
  print(x)

#Accessing string characters

str = 'Intelligent'

print('str = ', str)

#first character

print('str[0] = ', str[1])

#last character

print('str[-1] = ', str[-1])

#slicing 2nd to 5th character

print('str[1:5] = ', str[1:6])

#slicing 6th to 2nd last character

print('str[5:-2] = ', str[7:-2])  

#Iterating 

count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')

#String Slicing

Str1 = 'Ahimsa Jain'

print("\nSlicing characters from 2-9: ",Str1[2:9])
print("Slicing characters between 3rd and 2nd last character: ",Str1[3:-2])
print("Reversing of string: ",Str1[::-1])

# String Length

a = "I am going Bombay"
print(len(a))

# Check String

txt = "They are coming to our home today"
print("to" in txt)

txt = "They are coming to our home today"
print("but" in txt)

# Upper Case

a = "Okay bye!"
print(a.upper())

# Lower Case

a = "Hello, World!"
print(a.lower())

# Replace String

a = "Abdul Kalam!"
print(a.replace("b", "B"))

# Split String

a = "Hello, World!"
print(a.split(" .. ,  .."))

