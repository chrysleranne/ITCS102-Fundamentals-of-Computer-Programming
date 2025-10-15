isOdd = True
name = input("Hi, what is your name --> ")
print("\n++++++++++++++++++++++++++++++++++++++ \n\nODD NUMBER SELECTOR, press 0 to stop the loop \n\n++++++++++++++++++++++++++++++++++++++")
sum = 0
odd = ""

while isOdd == True :
    num = eval(input("Enter a random number:  "))
    if num %2 != 0:
        print("ODD NUMBER DETECTED")
        sum += num
        odd +=str(num) + " "
        continue
    elif num == 0:
        print("Loop Terminated")
        break

    else:
        if num %2 == 0:
            print("EVEN NUMBER IS DETECTED")
        else:
            print("invalid number / input")
        continue

print(f"Hi {name},The sum of all odds is {sum}")
print(f"ODD numbers include the ff --> {odd}")
