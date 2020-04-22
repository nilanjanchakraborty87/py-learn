
#! /usr/bin/python

import sys
from utils import power, repeat

"""
 Hello python
"""
def main():
    # print("Hello ", sys.argv[1])
    print("Square of 9: ", power(9, 2))
    print("Docstring of power: ", power.__doc__)
    print("power type: ", type(power))
    print(repeat("Python", 3))
    print(repeat("-", 100))

if __name__ == "__main__":
    main()
    


