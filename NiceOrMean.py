nice = 0
mean = 0

def main():
    start()

def start():
    print "Hello and welcome to Nice or Mean!"
    name = raw_input("What's your name? :")
    print "Hello "+name+"!"
    print "In this game, you will be greated by serveral different people. You can treat them nicely or you can be mean."
    print "At the end of the game, your fate will be determined by how you acted."

    choice = raw_input("Do you want to play? y/n" )

    if choice =="y":
        print "Great, use 'm' for mean and 'n' for nice"
        begin()
        
    if choice =="n":
        print "Okay, bye...."

    if choice != "y"+"n":
            choice = raw_input("Did you want to start playing? Please type Y/N ")

            if choice == "y":
             begin()
            
            if choice == "n":
             print "See you Later!"
             exit()

            if choice != "y"+"n":
                print "You're an idiot...."
                exit()

def begin():
    global nice
    global mean

    if nice > 2:
        print "Nice job, you win! Everyone loves you and you live in a palace."
        nice = 0
        choice = raw_input("Do you want to play again? y/n ")

        if choice == "y":
                print "Okay let's go!"
                nice = 0
                begin()
        
        if choice == "n":
                print "Say no more...Bye!"
                exit()

        elif choice != "y"+"n":
            print "Please enter Y or N"

    if mean > 2:
        print "Too bad - Game Over! You live in a van down by the river!"
        mean = 0

        choice = raw_input("Do you want to play again? y/n ")

        if choice == "y":
            print "Okay let's go!"
            mean = 0
            begin()

        if choice == "n":
            print "Say no more...Bye!"
            exit()

        elif choice != "y"+"n":
            print "Please enter Y or N"

        if choice == "y":
            Begin()
            
        if choice == "n":
            print "See you Later!"
            exit()

        if choice != "y"+"n":
            choice = raw_input("Do you want to play? Y/N ")

            if choice == "y"+"Y"+" y"+" Y":
             begin()
            
            if choice == "n"+"N"+" n"+" N":
             print "See you Later!"
             exit()

            if choice != "y"+"n":
                print "You're an idiot...."
                exit()


    pick = raw_input("Someone approaches you to talk, will you be nice or mean? n/m")

    if pick == "n":
            print "They smile, wave and walk away."
            nice = nice+1
            if nice >= 4:
                nice = 0
            print "You currently have " +str(nice)+" nice."
            begin()

    if pick == "m":
           print "They frown, glare at you and storm on."
           mean = mean+1
           if mean >= 4:
                mean = 0
           print "You currently have " +str(mean)+" mean."
           begin()

    
    



start()
