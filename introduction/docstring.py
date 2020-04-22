class hello:
    """This module demosnstrate the usage of python docstring"""
    default_message = "World"
    def __init__(self, message=default_message):
        #self.message = (hello.default_message, message)[message]
        self.message = message

    def greet(self):
        """an instance method to greet with the passing message"""
        print("Hello ", self.message)



if __name__ == "__main__":
    # way to create a python object
    obj = hello()
    # print class level doc string
    print(obj.__doc__)
    # call an instance method
    obj.greet()
    # print the instance method doc string
    print(obj.greet.__doc__)

    # create a new object with custom message
    obj1 = hello("Cognizant")
    obj1.greet()

            