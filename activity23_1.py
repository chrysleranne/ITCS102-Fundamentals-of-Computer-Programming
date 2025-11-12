def GreetName(name):
    print(f"Fighting, {name} you can do it!")

def GreetPerson(name, loc, age):
    print(f"Hi {name} from {loc}, {age} yr\'s old. ")

def FunctionReturn(number):
    print(f"This function calculates the summation from 1 to {number}")
    sum = 0
    for c in range(1, number +1, 1):
        sum += c
    return sum

def factorial(number):
    print(f" This function calculates the summation from 1 to {number}")
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact