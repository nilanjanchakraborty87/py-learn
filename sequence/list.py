ll = [50, 230, 2, 980, 34, "strings", [1,2.4], (1,2)]
print(type(ll))


print(ll[-8::1])
print(ll[:-1])
print(ll[:])
print(ll[::-1])

ll[1] = "new_value"
print(ll)

ll.append(700)
ll.extend([1,2,3])

l1 = [3, 6, 1]
l2 = [4, 2, 9]

l3 = l1 + l2
print(l3)


ll[1:4] = ["one", "two", "three"]
print(ll)

del ll[0]
print(ll)

# list repeatation
a = [1,2,3]
repeated_a = a * 3
print(repeated_a)

# membership check
print(5 in a)


# iteration
for elem in a:
    print(elem, end = ", ")

print()
# comprehension
numbers = list(range(1, 11))
even_numbers = [element for element in numbers if element%2 == 0]
odd_numbers = [element for element in numbers if element%2 != 0]

print("Even numbers: ", even_numbers)
print("Odd numbers: ", odd_numbers)

# check length
print("Length: ", len(numbers))

# get the max element
print("Max element: ", max(numbers))

# min, sum, sorted
unsorted = [10, 12, 7, 76, 3, 1, 100]
unsorted.sort(reverse=True)

# inline sort
names = ["Cognizant", "TCS", "IBM", "Walmart", "MACY"]
# names.sort(key=len)
names.sort(key=lambda str_elem: str_elem[1], reverse=True)
print(names)


names = ["Cognizant", "TCS", "IBM", "Walmart", "MACY"]
print(sorted(names, key=lambda str_elem: str_elem[1] ))
print(names)
#print(unsorted)





