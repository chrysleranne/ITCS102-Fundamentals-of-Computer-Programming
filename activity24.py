from activity23_1 import *

print("WELCOME TO MY COMPILER PROGRAM")
name = input("Hi pips, what is your name?  ")

print(f"Hi {name}, select from the options sa baba")
print("A - Greet Name\nB - Greet with Name, Age, Location\nC - Triangle\nE - Exit")

isCont = True

while isCont == True:
    choice = input("Select from A - E :  ").lower

    if choice == "a":
        name = input("Please state your name:  ")
        GreetName(name)
        continue
    elif choice == "b":
        number = eval(input("Input any number:  "))
        print(f"Factorial of {number} is {(number)} ")
        continue
    elif choice == "c":
        pass
        continue
    elif choice == "e":
        print("Program Terminated . . . . ")
        break
    else:
        print("Invalid choice ")
        break