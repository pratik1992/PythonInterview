#!/usr/bin/env python

"""Using ducktyping to determine the input at runtime"""


def convert(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return str(s)

    return type(convert(s))
