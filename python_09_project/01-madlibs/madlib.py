def Mad_Libs_Game():
    name = input("Enter your name: ")
    place = input("Enter a place name: ")
    animal = input("Enter an animal name: ")
    verb = input("Enter an action (verb): ")
    adjective = input("Enter an adjective: ")
    
    print("\nAll inputs are saved! ✅")
    
    story = f"One day, {name} went to {place}. There, they saw a {adjective} {animal} that was {verb}. Seeing this, {name} was very surprised!"
    
    print("\nHere is your funny story: 🎉\n")
    print(story)
Mad_Libs_Game()