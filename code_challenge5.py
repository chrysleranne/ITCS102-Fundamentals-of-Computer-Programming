#Get the factorial of a number

number = eval(input("Enter a number -->"))
factorial = 1
for c in range (number,0,-1):
    print(c)
    factorial *= c
print("The factorial of a number is", factorial)