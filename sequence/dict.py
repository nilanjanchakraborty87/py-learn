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
import collections

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

    # membership test for dictionary keys
    # membership operations not supported for values
    assert 6 in adict

    # get a default value if key does not exist
    default_val = adict.get(100, 'HUNDRED')
    assert default_val == 'HUNDRED'

    # create a list from dictionary using bulit-in list method
    # creates a list from dict keys
    l = list(adict)
    print("Converted list: ", l)

    # fromkeys method
    # Return a new dictionary with keys from a sequence and value equal to defaultValue or None
    fdict = dict().fromkeys(range(1, 11), 'DEFAULT_VALUE')
    assert len(fdict) == 10
    print("fromkeys generated dictionary: ", fdict)

    # traverse a dictionary
    # creating a dictionary using compreshension
    sdict = {i: i**3 for i in range(1, 11)}
    for i in sdict:
        print("Key: {}, Value: {}".format(i, sdict[i]))

    # Traverse dict items in pairs
    for k, v in sdict.items():
        print("Key: {}, Value: {}".format(k, v))
    
    
    # dictionary comprehension
    udict = {k: v.upper() for k, v in adict.items()}
    print("Uppercase representation of dict values: ", udict)
    
    # remove a partiular key from dictionary and returns the asscoiated value
    number = udict.pop(5)
    assert number == 'FIVE'

    # remove an arbitary element pair
    pair = udict.popitem()
    assert len(udict) == 4
    print("Removed pair: ", pair)

    # deletes a particular item
    del udict[3]
    assert len(udict) == 3

    # remove all elements
    udict.clear()
    assert len(udict) == 0

    # delete reference itself
    del udict

    # return the all dictionary keys
    #assert isinstance(adict.keys(), collections.KeysView)

    # convert into list
    keys = list(adict.keys())
    print("Keys: ", keys)

    # return the all dictionary Values
    #assert isinstance(adict.values(), collections.ValuesView)

    # return the all dictionary values as list
    values = list(adict.values())
    print("Values: ", values)


    


test_dict_operations()