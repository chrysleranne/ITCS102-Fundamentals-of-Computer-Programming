#Ask user to input a temperature

temp = eval(input("Enter Temperature Outside -->"))

if temp >= 1 and temp <=20 :
    print("Temperature is Considered as Extremely Cold")
elif temp >= 21 and temp <=30 :
    print("Temperature is Considered as Moderately Cold")
elif temp >= 31 and temp <=37 :
    print("Temperature is Considered as Lukewarm")
elif temp >= 38 and temp <=45 :
    print("Temperature is Considered as Hot")
elif temp >= 46 and temp <=50 :
    print("Temperature is Considered as Boiling Hot")
elif temp >= 46 and temp <=50 :
    print("Temperature is Considered as Daangerous Temperature")

else:
    print("Invalid Temperature")