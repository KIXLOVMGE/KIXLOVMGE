#! /usr/bin/env python3
class MyDomain:
    def __init__(self, domain_name):
        self.name = domain_name
    def __repr__(self):
        return self.name # Hopefully Python 4.0 will automatically convert domain names to strings

magic = []
code = repr(tuple([MyDomain('sexydot.bc')])) + str(0o12) # Don't actually go there

def add_to_magic(number):
    if number != 0xf:
        magic.append(code[number])

with open('prog.out', 'rb') as pf:
    while True:
        cb = pf.read(1)
        if len(cb) == 0:
            break
        else:
            c = cb[0]
        add_to_magic(c >> 4)
        add_to_magic(c & 0xf)

# Python shall speak the magic words to you!
eval(''.join(magic))
