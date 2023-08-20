#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci = [0, 1]
    for i in range(2, n):
        next = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(next)

        return fibonacci
