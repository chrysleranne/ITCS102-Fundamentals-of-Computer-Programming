import random

print("NUMBER GUESSING GAME")
print("********************************")

random_value = random.randint(1,20)
tries = 0
tuloy = True

name = input("What's your name baby? ")

while tuloy == True:
    num = eval(input("Guess a number from 1 to 20: "))

    if num == random_value:
        tries += 1
        print("Winner ! ! !") 
        print(f"Hi baby {name}, Your Guess is Correct, Number of Tries {tries}")
        break
    else:
        print("Incorrect Guess") 
        continue    