"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random

# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print('pi type = ', type(pi), ' and pi value = ', pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50:
    print(i, ' is less than 50')
else:
    print(i, ' is equal or greater than 50')

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print('the picked fruit was orange color')
elif picked_fruit == 'strawberry':
    print('the picked fruit was red color')
else:
    print('the picked fruit was yellow color')

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def product(arg1, arg2):
    result = arg1 * arg2
    return result

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 = ", product(12, 96))

print("48 x 17 = ", product(48, 18))

print("196523 x 87323 = ", product(196523, 87323))
