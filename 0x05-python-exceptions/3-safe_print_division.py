#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, NameError):
        return None
    finally:
        print("inside result: None")
    return result

