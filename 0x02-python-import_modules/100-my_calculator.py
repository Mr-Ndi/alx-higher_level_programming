#!/usr/bin/python3
import sys
import calculator_1 as calc


number = len(sys.argv) - 1

if number != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
operat = sys.argv[2]

if operat not in ('+', '-', '*', '/'):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

if operat == '+':
    ans = calc.add(a, b)
elif operat == '-':
    ans = calc.sub(a, b)
elif operat == '*':
    ans = calc.mul(a, b)
elif operat == '/':
    ans = calc.div(a, b)

print("{} {} {} = {}".format(a, operat, b, ans))
