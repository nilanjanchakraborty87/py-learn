
# global
x = 10

# local
def func():
    y = 7
    #x = 8
    #global x
    x = 8
    print(x)
    print(y)  


func()            
print(x)

# enclosing
def outer():
    a = 7
    def inner():
        b = 9
        nonlocal a
        print("Nonlocal: ", a)
        print("Local variable: ", b)

        # now update nonlocal a
        a = 10
        print("Updated nonlocal: ", a)
    inner()
    print(a)

outer()



