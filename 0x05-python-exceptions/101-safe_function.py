#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        results = fct(*args)
        return results
    except IndexError:
        print("Exception: list index out of range", file=sys.stderr)
    except ZeroDivisionError:
        print("Exception: division by zero", file=sys.stderr)
