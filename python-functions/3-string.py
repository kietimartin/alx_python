#!/usr/bin/python3
def reverse_string(string):
    return string[::-1]
# we use slice to reverse the string

x = reverse_string('Hello world')
print(x)