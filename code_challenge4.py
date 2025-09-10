print("Welcome to Manga Recommender!")
print("Answer a few question to find your next read")
print("What genre do you like?")
print("1.Action")
print("2.Romance")
print("3.Horror")
genre_choice = input("Enter choice (1,2,3):")

if genre_choice == "1":
    genre = "Action"
    print("You selected: ",genre)
    input("How long the manga should be? (short, medium, long): ")
    era = input("Which decade? (2000s, 2010s): ")
        
    if era == "2000s":
        print("You want 2000s, here's my recommendations: ")
        print("1.Gantz")
        print("2.Death Note")
        print("3.Busou Renkin")
        print("Thank you, have a nice read")
    
    elif era == "2010s":
        print("You want 2010s, here's my recommendations: ")
        print("1.Soul Eater Not!")
        print("2.Seraph of the End")
        print("3.The Seven Deadly Sins")
        print("Thank you, have a nice read")

elif genre_choice == "2":
    genre = "Romance"
    print("You selected: ",genre)
    input("How long the manga should be? (short, medium, long): ")
    era = input("Which decade? (2000s, 2010s): ")
        
    if era == "2000s":
        print("You want 2000s, here's my recommendations: ")
        print("1.Love My Life")
        print("2.Hana-Kimi")
        print("3. Fruits Basket")
        print("Thank you, have a nice read")
    
    elif era == "2010s":
        print("You want 2010s, here's my recommendations: ")
        print("1.A Silent Voice")
        print("2.My Love Story")
        print("3.Strobe Edge")
        print("Thank you, have a nice read")

elif genre_choice == "3":
    genre = "Horror"
    print("You selected: ",genre)
    input("How long the manga should be? (short, medium, long): ")
    era = input("Which decade? (2000s, 2010s): ")
        
    if era == "2000s":
        print("You want 2000s, here's my recommendations: ")
        print("1.Parasyte")
        print("2.Claymore")
        print("3.Jigoku Shoujo")
        print("Thank you, have a nice read")
    
    elif era == "2010s":
        print("You want 2010s, here's my recommendations: ")
        print("1.Tokyo Ghoul")
        print("2.Deadman Wonderland")
        print("3.Corpse Party")
        print("Thank you, have a nice read")