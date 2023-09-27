#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = abs(number) % 10

if number < 0:
    last_number_sign = last_number * -1
else:
    last_number_sign = last_number

if last_number_sign > 5:
    print(f'Last digit of {number} is {last_number_sign} and is\
 greater than 5')
elif last_number_sign == 0:
    print(f'Last digit of {number} is {last_number_sign} and is 0')
else:
    print(f'Last digit of {number} is {last_number_sign} and is\
 less than 6 and not 0')
