#!/usr/bin/env python

abc = ['dog', 'Fido', 10]

output = ('{name} the {animal} is {age} years old '.format(name=abc[1], animal=abc[0], age=abc[2]))

print output
