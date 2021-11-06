#Write a Python program to get a single string from two given strings, separated by a space 
# and swap the first characters of each string.

str1 = 'abc'
str2 = ' xyz'

print((str1.replace("a", "x")) + (str2.replace("x", "a")))
