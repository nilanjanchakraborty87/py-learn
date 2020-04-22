"""Dictionary

Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array. 
A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value

Dictionary is mutable and unordered. It can be nested and can contain mixed of datatypes

You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). 
A colon (:) separates each key from its associated value.

A Dictionary can be declared in following way

adict = {
    k1: v1, 
    k2: v2, 
    k3: v3
}

Declare an empty dictionary :

adict = {}

You can also construct a dictionary with the built-in dict() function. 

The argument to dict() should be a sequence of key-value pairs. 

We can create a dictionary from list of tuples as follows

adict = dict({
    (k1, v1),
    (k2, v2),
    (k3, v3)
}) 

if keys are simple strings you can also create a dictionary in following way

adict = dict(
    nilanjan='36',
    anupam='35'
)

"""

def test_is_dict():
    # declare a dictionary
    adict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }
    # print dictionary type
    print(type(adict))

    # verify whether its a dictionary
    assert isinstance(adict, dict)

    # verify length of a dictionary
    assert len(adict) == 5

test_is_dict()

def test_dict_operations():
    # declare a dictionary
    adict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }

    # access an element from dict
    assert adict[3] == 'three'

    # you can also access using a dictionary element using get() method 
    assert adict.get(3) == 'three'

    # access using associative array index expression throws KeyError exception
    #print(adict[8])

    # get() method returns None instead if the key does not exist
    print(adict.get(8))

    # update a dictionary element
    adict[1] = 'ONE'
    assert adict[1] == 'ONE'

    # add a new element into dictionary
    adict[6] = 'Six'
    assert len(adict) == 6
    
    

test_dict_operations()