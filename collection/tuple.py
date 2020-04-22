"""Tuples

A script to explain all tuple related operations.

Tuple is a python data structure/collection which is an immutable sequence. It is quite similar
to the list but it's elements can not be changed

Tuples can be declared in following way

a_tuple = (1,2,3,4)

To declare a tuple, wrap elements (parentheses)

You can also declare an empty tuple as

a_tuple = ()

Parentheses are optional, however we should use it

Remember tuple supports mixed datatypes

"""

def test_empty_tuple():
    # empty tuple declaration
    a_tuple = ()
    # empty check
    assert len(a_tuple) == 0

test_empty_tuple()

def test_singleton_tuple():
    """ 
        shows how to create a tuple with single element
    """
    a_tuple = (1,)
    assert len(a_tuple) == 1

test_singleton_tuple()

def test_tuple_operations():
    # tuple contains multiple datatypes
    a_tuple = (1, 2, "A string value", 7.5, [5,6,7], 1)
    assert len(a_tuple) == 6
    
    # Tuple can also be created using the built-in tuple() function. You can pass any sequence to the 
    # tuple() function to create a tuple from any existing sequence
    b_tuple = tuple(range(5, 11))

    # print tuple
    print("Tuple : ", a_tuple)

    # access tuple elements with indexing
    print("Tuple second element: ", a_tuple[1])

    assert a_tuple[2] == "A string value"

    # tuple reverse indexing 
    assert a_tuple[-3] == 7.5

    # slicing on tuple
    # Note: end_index in exclusive
    print("Tuple first 3 elements: ", a_tuple[:3])

    # reverse a tuple
    # Note: slicing supports -> start_index:end_index:step
    print("Reversing a tuple tuple: ", a_tuple[::-1])

    # tuple is immutable, hence can not be modified
    # it is not supported 
    # Note: this raises TypeError: 'tuple' object does not support item assignment
    # a_tuple[1] = "Updated value"

    # count an element count in tuple
    print("Element 1 total count: ", a_tuple.count(1))

    # check indexof element in tuple
    # Note: it returns the first index of matched element
    assert a_tuple.index(1) == 0

    # nested tuple
    n_tuple = ((1,2,3), (3,4,5), (5,6,7))
    assert n_tuple[1][0] == 3

    # append 
    print("a_tuple + b_tuple: ", a_tuple + b_tuple)

    # delete a tuple
    del a_tuple
    # raises error: UnboundLocalError: local variable 'a_tuple' referenced before assignment
    # assert isinstance(a_tuple, tuple)

    # repeat
    print("b_tuple repeat: ", b_tuple * 2)

    a_tuple = tuple(range(1,4))

    # unpack a tuple
    x, y, z = a_tuple

    assert x == 1
    assert y == 2
    assert z == 3

    # membership test in tuple
    assert x in a_tuple

    # not a member check
    assert 4 not in a_tuple

    # iterating a tuple
    for item in a_tuple:
        print("Tuple item: ", item)

    # Note there is no comprehension for tuple rather it is called generator
    another_tuple = tuple(i**2 for i in (1, 2, 3))
    print("Tuple genarated using generator: ", another_tuple)



    
test_tuple_operations()



