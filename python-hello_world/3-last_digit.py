#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#we use modulo to get the last digit
last_digit = abs(number)
last_digit = last_digit % 10

#set the conditions
#greater than 5
if (last_digit > 5):
        print('Last digit of {} is {} and is greater than 5'.format(number, last_digit))

#is 0
elif (last_digit == 0):
    print('Last digit of {} is {} and is 0'.format(number, last_digit))

#is less than 6 and not 0
elif (last_digit < 6) and (last_digit != 0):
    if (number > 0):
        print('Last digit of {} is {} and is less than 6 and not 0'.format(number, last_digit))
    elif (number < 0):
        print('Last digit of {} is -{} and is less than 6 and not 0'.format(number, last_digit))