#! /usr/bin/env python3

"""
greet the world
"""

x = 10
y = 5

z = x/y
print(type(z))

zz = x//y
print(type(zz))

ll = [1, 2, 3, 4, 5]

for i in ll:
    print(i)

lsq = [ i**2 for i in ll if i%2 == 0]
lsq1 = [ "Even " + str(i) if i%2 == 0 else "Odd " + str(i) for i in range(10)]
print(lsq)
print(lsq1)


for i in range(10):
    print(i, end=' ')

print()

for i in range(1, 11):
    print(i, end = ' ')

print() 

for i in range(1, 11, 2):
    print(i, end = ' ')

print()

for i in range(10, 0, -1):
    print(i, end = ' ')