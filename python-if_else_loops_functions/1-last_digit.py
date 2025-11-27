#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    print(f"Last digit of {number} is -{abs(number) % 10} and i"
          f"s less than 6 and not 0")
else:
    print(f"Last digit of {number} is {number % 10} and is " +
          ("0" if number == 0 else "greater than 5"))
