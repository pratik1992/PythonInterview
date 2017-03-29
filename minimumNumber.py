#!/usr/bin/env python


def find_minimum(num1=None, num2=None, num3=None):
    if num1 is None and num2 is None and num3 is None:
        print "Please provide three numbers"

    elif (num1 < num2) and (num1 < num3):
        smallest = num1

    elif (num2 < num1) and (num2 < num3):
        smallest = num2

    else:
        smallest = num3

    print ("The smallest number is {largest}".format(largest=smallest))


