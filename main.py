print("CyberPunk 2049 Text adventure")
# User Input
name = input("What is your name? ")
age = int(input("What is your age? "))
gender = input("What is your gender? ")
race = input("What is your race? ")
#skills = input("")
#male = ("he, his, brother")
#female = ("Her, sister")
# Prints back User's name and age
print("Hello", name, "you are a",age, "year old", gender,)

#if gender == male:
    #print("he")

#if gender == female:
    #print("her")

if age >= 18:
    print("You are old enough to play!")
    
    want_to_play = input("Do you want to play? ")
    if want_to_play == "yes":
        print("Welcome to Cyperpunk 2049 text adventure!")
        
        
        
        Nomad_or_Corpo = input("Normad or Corpo (Nomad/Corpo)? ")
        if Nomad_or_Corpo == "Corpo":
            print("Another Corpo rat looking to take the throne..."
                  "You stare blankly at your montior as the string of numbers flow on your screen, just another day in the office. "
                        "You zip a call to one of your co-workers. How much longer till you send those reports?"
                        "I'm sorry...", name, "But I need a little more time... ")
            
            
            Threaten_or_Pursuade = input(" (Threaten/Pursuade)?")
            if Threaten_or_Pursuade == "Threaten":
                print("Look you don't wanna make Eve angry, otherwise I'll have to pay a late night visit to yout mother in" 
                      "the mental ward "
                      "Sorry...I'll have those reports by midnight", name,
                      " We'll it's about fucking time I needed those reports by fucking yesterday Jensen! "
                      "You ended the call, a few minutes pass before you get the reports."
                      "a call pops up it's from Eve"
                      "Office now.", name,
                      "You head up towards the head offices "
                      "(You were greeted with her back towards you and the grand lights of night city illumanting the dark office)"
                      "Sit", name,"."
                      "Alright, are going to tell me what's this about"
                      "Night city, our competiors and the future of Yin tech."
                      "And what's this got to do with me,"
                      "I want to promote you to my knight, you protect me and I'll return the favor sometime down the road when I see fit. "
                      "Gee thanks."
                      "Don't tell me you don't want same thing as me to see the world where others can only wish it in their dreams", name, 
                      "Do the right thing and help me")
                
            else:
                Pursuade = print("Look I get it your new to Yin tech, but if you help me out here I'll make sure your mother upgrades "
                                 "to Tramua team platuim overnight free of charge."
                                 "Alright, alright... Truth is I actually been had those reports done but we've been getting a infulx of new data from our netrunner, "
                                 " we're on the verge getting the one up on Araska! I just wanted those reports to be the most recent as possbile."
                                 "Christ Jensen why didn't say anything sooner!"
                                 "Sorry...", name, " But could we keep this between us only... I get it you want to knock the bitch Eve off her throne but."
                                 "Even if what you say is true about getting me Tramua team platuim, I rather do it on my own terms instead of dirtying my hands with blood.. "
                                 "It'll be better for the both us if we just wait this out...")
                
                Pressure_or_Playitsafe = input("(Pressure/play it safe)")
                if Pressure_or_Playitsafe == "Pressure":
                    print("Christ! You've kept this hidden for god knows how long and you want to keep this hidden... The fucks wrong with you Jensen! "
                          "I know", name, "I just wanted to play things on my own terms! I don't want to be another souless corpo!"
                          "Look kid you sold your soul the moment you signed with contract Yin tech"
                          "...", name, "...Meet me in front of Eden"
                          "The call ends.")
                
                
        
        else:
            Nomad = ("")
        
        stars_or_fire = input(" You chosed the freedom of the roads.(stars/fire)")
        if stars_or_fire == "stars":
            ans = input("You look up at the stars surronded by your clan sharing their latest adventures of the badlands")
    
    
    
    
    else:
        print("See ya...")
    
else:
    print("You are not old enough to play...")

