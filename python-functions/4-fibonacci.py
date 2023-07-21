#!/usr/bin/python3
def fibonacci_sequence(n):
    for n in range(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci_sequence(n-2) + fibonacci_sequence(n-1)


print(fibonacci_sequence(5))