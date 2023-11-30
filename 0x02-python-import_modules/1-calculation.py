#!/usr/bin/python3
import calculator_1 as cal


if __name__ == '__main__':
    a = 10
    b = 5
    summ = cal.add(a, b)
    diff = cal.sub(a, b)
    pro = cal.mul(a, b)
    quo = cal.div(a, b)
    print("{} + {} = {}".format(a, b, summ))
    print("{} - {} = {}".format(a, b, diff))
    print("{} * {} = {}".format(a, b, pro))
    print("{} / {} = {}".format(a, b, quo))
