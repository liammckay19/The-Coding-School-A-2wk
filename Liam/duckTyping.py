s = 'asldjkfhasdf'
s = 19
s = [1, 4, 5]


# dynamically typed - we don't have to define the object type at initialization

def function(x, y=None):  # also we don't have to define argument types
    if y is None:
        return x
    elif type(x) == int() and type(y) == int():
        return x ** 2, y ** 2
    else:
        return x, y


# cannot do method overloading in python

function(1, 2)
function("a", "b")
function(1)


class Duck:
    def quack(self):
        print("Quack!")


class Dog:
    def bark(self):
        print("Woof!")
        
    def quack(self):
        print("Quack!")


donald = Duck()
carl = Dog()
donald.quack()
carl.quack()
