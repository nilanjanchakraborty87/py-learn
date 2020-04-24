"""NamedTuples

The standard tuple uses numerical indexes to access its members.

for eg. atuple = (1, 5, 7)
assert atuple[1] == 5

But remembering which index should be used for each value can lead to errors, 
especially if the tuple has a lot of fields.

A downside is that the data you store in them can only be pulled out by accessing it through integer indexes. 
You can’t give names to individual properties stored in a tuple. This can impact code readability.

Additionally a tuple is always an ad-hoc structure. It’s hard to ensure that two tuples 
have the same number of fields and the same properties stored on them. 
This makes it easy to introduce bugs by mixing up the field order.

Namedtuples aim to solve above problems.

A namedtuple assigns names, as well as the numerical index, to each member. 
Hence each object stored in them can be accessed through a unique (human-readable) identifier

namedtuples are also immutable just like regular tuples. Once you store something in them you can’t modify it.

To use namedtuples you need to import the collections module.

from collections import namedtuple
Product = namedtuple('Product' , 'name brand category color')

Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. 
The arguments are the name of the new class and a string containing the names of the elements


The namedtuple creation syntax a little weird. We pass the fields as a string encoding with 'Space' separated 
"name brand category color"

namedtuple’s factory function calls split() on the field names string.

Hence we can also pass a list with string field names directly if we prefer.

For eg. 

Product = namedtuple('Product' , [
    'name',
    'brand',
    'category',
    'color'
])

Now we can create new “product” objects with the Product factory function. 

product1 = Product('Mobile Phone', 'Samsung', 'Phones', 'Red')

Now we can access product1 attributes like

assert product1.color == 'Red'

Namedtuples can be an easy way to clean up your code and to make it more readable 
by enforcing a better structure for your data.

Like tuples, namedtuples are immutable. When you try to overwrite one of their fields you’ll get 
AttributeError exception:

product1.color = 'Blue'
AttributeError: "can't set attribute"

Remeber:
    Using namedtuples over unstructured tuples and dicts can also make our code more readable and maintenanble.
    Need to import namedtuple from collections module



"""

from collections import namedtuple

def test_namedtuple_creation():
    """
        created a named tuple
    """

    Person = namedtuple('Person', 'name age gender')

    # check type of person
    print("Type of person: ", type(Person))

    # now lets create few peron objects
    john = Person(name = "John Doe", age = 35, gender = "MALE")
    # access namedtuple attributes
    assert john.age == 35

    # create another person object
    jane = Person(name = "Jane Doe", age = 32, gender = "FEMALE")
    assert jane.age == 32


test_namedtuple_creation()

def test_namedtuple_operations():

    Person = namedtuple('Person', 'name age gender')

    # now lets create few peron objects
    john = Person(name = "John Doe", age = 35, gender = "MALE")

    # now print a namedtuple
    print('%s is %d year old %s' % (john))

test_namedtuple_operations()