#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastnum = number % 10
else:
    lastnum = (abs(number) % 10) * -1
message1 = " and is greater than 5"
message2 = " and is 0"
message3 = " and is less than 6 and not 0"
if lastnum > 5:
    print("Last digit of {} is {}".format(number, lastnum) + message1)
elif lastnum == 0:
    print("Last digit of {} is {}".format(number, lastnum) + message2)
else:
    print("Last digit of {} is {}".format(number, lastnum) + message3)
