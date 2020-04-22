def greet(*args, **kwargs):
    """
    docstring
        this function takes a message and greets you
    """
    print("Hello ", args[0], args[1], args[2])
    print("Kwargs ", kwargs["message"])

# greet("Cts", "Macy", "IBM", message = "Nilanjan")
print(greet.__doc__)

# lambda
# multipler_3 = 

"""
def random11111(x): 
    print(x)

func = random11111
"""

for i in range(1, 11):
    #print((lambda x: 3 * x)(i))
    pass

# dunder __repr__/__str__
# object

func = lambda msg = "World": print("Hello, ", msg)
func()
func("Naga")

func = lambda : print("Example lambda")
func()