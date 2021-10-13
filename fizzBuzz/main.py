#!/usr/bin/env python3

# import sys

# sys.tracebacklimit = 0

# def test(n1, n2):
#     print(int(n1*n2))

# def manageInput(input):
#     try:
#         return float(input)
#     except ValueError:
#         exit('exit: must enter a digit')

# number1 = manageInput(input('add a number: '))
# number2 = manageInput(input('multiply by: '))

# test(number1, number2)

# input('press any key to exit')


# listOfIntegers = list(range(0, 100))

import fizzBuzz

input = open('input.txt', 'r')
res = open('res.txt', 'w+')
fb = fizzBuzz.FizzBuzz

fb.exec(res, fb.utils.parse(input))
res.close()
input.close()