print("ODD NUMBER ACCUMULATOR")
print("Enter 10 numbers. We'll sum only the odd ones!\n")
odds = 0

for c in range(1,11,1):
    num = eval(input("Enter a number:"))
    if num % 2 != 0:
        odds += num
        
print("\nSum of all odd number:", odds)
