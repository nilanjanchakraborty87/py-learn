"""Sets

A script to explain all set related operations.

Set is a python data structure/collection which is unordered. It does not 
support index also. 

Sets can be declared in following way

aset = {1,2,3,4}

Set does not allow duplicates and it supports the below mathematical operations like 
union, intersection, difference etc

Remember you can't declare any empty set with empty braces for eg. 

empty_set = {} # this will be inferred as dictionary object in python

The type of the above empty collection would be dictionary instead of set 

"""

def test_set():
    """
        Test whether a declared collection is a set or not
    """
    #declares a set
    cars = {"Honda", "Maruti", "Chevrolet"}
    assert isinstance(cars, set)

    # also we can construct set in below way
    # for eg. we have list of numbers from 1..10
    numbers = list(range(1, 11))

    # lets repeat the list. List will contain duplicates now 
    numbers *= 3

    # now convert the above list to set which will drop all the duplicate numbers from list and creates the list
    # using set function
    unumbers = set(numbers)

    # let's test the data type
    assert isinstance(unumbers, set)

    assert len(unumbers) == 10

    # we can also print the datatype
    print("unumbers is a {0} datatype".format(type(unumbers)))


test_set()

def test_set_operations():
    """
    We will show all the supported set operations in this function
    """

    #declares a set
    cars = {"Honda", "Maruti", "Chevrolet"}

    # length of set
    assert len(cars) == 3
    print("Length of set: {}".format(len(cars)))

    # test whether an element exists in set
    assert "Honda" in cars
    
    # not existence check
    assert "BMW" not in cars

    # add operation will append the item at the end of the set
    # using add function you can append a single element to set
    cars.add("BMW")
    assert len(cars) == 4
    print("Current set snapshot (after add operation): ", cars)

    # use update function to append an iterable to set
    cars.update(['Tata', 'Ford', 'Hyundai'])
    assert len(cars) == 7 
    print("Current set snapshot (after update operation): ", cars)

    # remove operation to remove a particular element from set
    # remove raises exception of the target element does not exist
    cars.remove("Chevrolet")
    assert len(cars) == 6
    print("Current set snapshot (after remove operation): ", cars)

    # there is a similar method like remove in set, called discard
    # discard does now raise exception
    cars.discard('Skoda')
    # though skoda does not exist in our set, it does not raise any exception
    # cars length will remain same
    assert len(cars) == 6

    # we can also use pop method to remove an element
    # a arbitary is removed and returned
    popped_brand = cars.pop()
    # cars length will become 5
    assert len(cars) == 5
    # this is unpredictable which element will be removed. Hence be careful before using this method
    print("Popped brand: ", popped_brand)   

    # set comprehension to convert each brand letters into uppercase letters
    BRANDS = {brand.upper() for brand in cars}
    print("Car brands: ", BRANDS)


test_set_operations()


def test_set_mathematical_operations():
    """
    In this function we will use various mathematical set operations and observer their behavior
    """

    # let's declare two sets
    # A set contains numbers 1..5
    A = set(range(1, 6))
    assert len(A) == 5
    print("A set snapshot: ", A)

    # B set contains numbers 6..10
    B = set(range(6, 11))
    assert len(A) == 5
    print("B set snapshot: ", B)

    # Now let's do an union operation using the overloaded PIPE operator
    C = A | B
    # C set size would be 10
    assert len(C) == 10
    print("Union set (created using | operator) snapshot: ", C)

    # we can also use the union method also
    UC = A.union(B)
    assert len(UC) == 10
    print("Union set (created using union method) snapshot: ", UC)

    # intersection operation
    # using overloaded & operator
    AA = set(range(1, 11))
    BB = set(range(5, 16))

    # intersection output creates a new set
    I = AA & BB
    assert len(I) == 6
    print("intersection (using operator) set snapshot: ", I)

    # we can also use the intersection method
    I = AA.intersection(BB)
    assert len(I) == 6
    print("intersection (using method) set snapshot: ", I)
    
    # difference operation
    # using overloaded - operator

    D = BB - AA
    assert len(D) == 5
    # just took another approach to compare the contents
    assert D == {11, 12, 13, 14, 15}
    print("set created using difference operation snapshot: ", D)

    # using the differce method
    D = BB.difference(AA)
    assert len(D) == 5


test_set_mathematical_operations()