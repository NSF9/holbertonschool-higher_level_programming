#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


Last_Digit = abs(number) % 10

if Last_Digit > 5:
    
    print(f"Last digit of {number} is {Last_Digit} and is Greater than 5")
elif Last_Digit == 0:
    print(f"Last digit of {number} is {Last_Digit} and is 0")
else:
      print(f"Last digit of {number} is {Last_Digit} and is less than 6 and not 0")
