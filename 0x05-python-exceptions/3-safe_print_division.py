#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result:
            print("Inside resul:{:.1f}".format(result))
        else:
            print("Inside resul:{}".format(result))
    return result
