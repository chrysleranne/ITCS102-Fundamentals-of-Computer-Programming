Legit = True
list = [ ]
name = input("What is your name? ")
print(f"Hi {name}, Welcome to Anime Lister")

while Legit == True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ").lower()
  
    if anime != 'exit':
        print(f"'{anime}' has been added to your anime list.")
        list.append(anime)
        continue

    elif anime == 'exit':
        print("\nYou have exited the anime enrty program.")
        break

    else:
        print("Please try again")

print("Your anime list includes:")
for anime in list:
	print(f"- {anime}")

