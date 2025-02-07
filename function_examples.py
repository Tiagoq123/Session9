def greet():
    """
    Simple function that prints "Hello!"
    :return:
    """
    print("Hello!")
    return 0

def greet_improved(name):
    """
    More complex greet that takes a name as param
    :param name: the name of the person to greet
    :return: none
    """
    print("Hello", name)
greet_improved("Felipe")
greet_improved("Noam")

def custom_op(x=0, y=0):
    """
    Custom op: 10x+y
    :param x: the first number
    :param y: the second number
    :return: number, 10x+y
    """
    result = 10*x +y
    return result

print(custom_op(5,8))
x = custom_op(5,9) # arguments by position!
print(f"the result of custom_op is: {x}")
x= custom_op(y=9, x=5) #arguments by name!
print(f"the result of custom_op is: {x}")
print(custom_op(5)) #using default values for y
print(custom_op()) # default values for both
print(custom_op(y=9)) # default value for x

def bond_intro(name):
    print("the name is:", name)

def bond_name(first, last):
    return f"{last}, {first} {last}"

print(bond_name("Tiago", "Quevedo"))
bond_intro(bond_name("Tiago", "Quevedo"))
bond_intro(bond_name())

