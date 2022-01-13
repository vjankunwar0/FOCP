print("Stop! Who would cross the Bridge of Death")
print("Must answer me these questions three, 'ere the other side he see.")

#Asks for a name 
name_py=input("What is your name?")


#Checks if he is king or not
if name_py.capitalize()=="Aurther":
    print("My liege! You may pass!")
else:
    #Asks for the quest
    quest_py = input("what is your quest?")
    #checks if the quest contains "grail" or not
    if "grail" in quest_py.lower():
        
        #Asks for the favourite colour
        colour_py = input("What is your favourite color?")

        #Checks if the first letter of the name and colour is same or not
        if colour_py[0].upper() == name_py[0].upper():
            print("You may pass!!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
    
    else:
        print("Only those who seel the (Grail) may pass")


    
