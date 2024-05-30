#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_numbers = []
    
    for i in range(length):
        if i == 0:
            fibonacci_numbers.append(0)
        elif i == 1:
            fibonacci_numbers.append(1)
        else:
            fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    
    print(fibonacci_numbers)


    