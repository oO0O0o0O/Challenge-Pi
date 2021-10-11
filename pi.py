'''
Calculates pi using a function that evenly generates numbers
from 0 to 1.
'''

from random import random

def main():
    # Define counters for points
    total = 0
    inside = 0

    # Plot 1000 points
    for i in range(1000):
        x = random()
        y = random()

        # Check if point inside circle
        if x**2 + y**2 <= 1:
            inside += 1
    
        total += 1
    
    pi = 4*inside/total

    print("Points: {}\nPi: {:.2f}".format(total, pi))

main()