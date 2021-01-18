print("CyberPunk 2049 Text adventure")
# User Input
name = input("What is your name? ")
age = int(input("What is your age? "))
gender = input("What is your gender? ")
# Prints back User's name and age
print("Hello", name, "you are a",age, "year old", gender,)

if age >= 18:
    print("You are old enough to play!")
    
    want_to_play = input("Do you want to play? ")
    if want_to_play == "yes":
        print("Welcome to Cyberpunk 2049 text adventure!")
        
        
        
        Nomad_or_Corpo = input("First choice...Normad or Corpo (Nomad/Corpo)? ")
        if Nomad_or_Corpo == "Corpo":
            print("Another Corpo rat looking to take the throne...You stare blankly at your montior as the string of numbers flow on your screen, just another day in the office. "
                        "You zip a call to one of your co-workers. How much longer till you send those reports?"
                        "I'm sorry...", name, "But I need a little more time... ")
            
            
            Threaten_or_Pursuade = input("Second choice (Threaten/Pursuade)?")
            if Threaten_or_Pursuade == "Threaten":
                print("Look you don't wanna make the boss angry, otherwise I'll have to pay a late nigt visit to yout mother in" 
                      "the mental ward")
                
            else:
                Pursuade = ("")
                
                
                
        
        else:
            Nomad = ("")
        
        stars_or_fire = input(" First choice...You chosed the freedom of the roads.(stars/fire)")
        if stars_or_fire == "stars":
            ans = input("You look up at the stars surronded by your clan sharing their latest adventures of the badlands")
    
    
    
    
    else:
        print("See ya...")
    
else:
    print("You are not old enough to play...")

