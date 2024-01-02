#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = abs(number) % 10
elif number > 0:
    lastdigit = number % 10
else:
    lastdigit = number
if number >= 0:
    if (lastdigit < 6) & (lastdigit != 0):
        print(f"Last digit of {number} is \
{lastdigit} and is less than 6 and not 0")
    elif (lastdigit > 5) & (lastdigit != 0):
        print(f"Last digit of {number} is {lastdigit} and is greater than 5")
    else:
        print(f"Last digit of {number} is {lastdigit} and is 0")
else:
    if lastdigit == 0:
        print(f"Last digit of {number} is {lastdigit} and is 0")
    else:
        print(f"Last digit of {number} is \
-{lastdigit} and is less than 6 and not 0")
