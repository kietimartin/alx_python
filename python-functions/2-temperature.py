#!/usr/bin/python3
def convert_to_celsius(fahrenheit):
    if (fahrenheit < 0):
        fahrenheit = round((fahrenheit - 32) * (5/9), 2)
        return fahrenheit
    
    else:
        fahrenheit = (fahrenheit - 32) * (5/9)
        return fahrenheit