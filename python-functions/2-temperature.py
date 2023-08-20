#!/usr/bin/python3
def convert_to_celsius(fahrenheit):
    fahrenheit = (fahrenheit - 32) * (5/9)
    print('{:2d}'.format(fahrenheit))