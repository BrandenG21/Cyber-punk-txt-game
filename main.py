print("CyberPunk 2049 Text adventure")
# User Input
name = input("What is your name? ")
age = int(input("What is your age? "))
gender = input("What is your gender? ")
male = ("he, his")
female = ("Her")
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
                print("Look you don't wanna make the boss angry, otherwise I'll have to pay a late night visit to yout mother in" 
                      "the mental ward "
                      "Sorry...I'll have those reports by midnight", name,
                      ",We'll it's about fucking time I needed those reports by fucking yesterday Jensen! "
                      "You ended the call")
                
            else:
                Pursuade = print("Look I get it your new to Yin tech, but if you help me out here I'll make sure your mother upgrades "
                                 "to Tramua team platuim overnight free of charge."
                                 "Alright, alright... Truth is I actually been had those reports done but we've been getting a infulx of new data from our netrunner, "
                                 " we're on the verge getting the one up on Araska! I just wanted those reports to be the most recent as possbile."
                                 "Christ Jensen why didn't say anything sooner!"
                                 "Sorry...", name, " But could we keep this between us only... I get it you want to knock the bitch Eve off her throne but..."
                                 "Even if what you say is true about getting me Tramua team platuim, I rather do it on my own instead of dirtying my hands with sin ")
                
                Pressure_or_Playitsafe = input("(Pressure/play it safe)")
                if Pressure_or_Playitsafe == "Pressure":
                    print("")
                
                
        
        else:
            Nomad = ("")
        
        stars_or_fire = input(" First choice...You chosed the freedom of the roads.(stars/fire)")
        if stars_or_fire == "stars":
            ans = input("You look up at the stars surronded by your clan sharing their latest adventures of the badlands")
    
    
    
    
    else:
        print("See ya...")
    
else:
    print("You are not old enough to play...")

