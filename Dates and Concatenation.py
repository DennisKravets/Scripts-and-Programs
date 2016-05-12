print "Let's say the date is 11/12/2013"
originalAsk = raw_input("Would you like to see how we can arrange this in code and get rid of the '/' marks? Y/N ")

if originalAsk == "y":

    #Go through string and split numbers by ('/')
    date = "11/12/2013"

    date_manip = date.split('/')

    print date_manip

    print date_manip[0]
    print date_manip[1]
    print date_manip[2]
    
elif originalAsk == "n":
    quit()

#Decide if they want to continue
decide = raw_input("Would you like to break it down some more? Y/N")

#If they decide yes, execute script otherwise quit
if decide == "y":

    print "Month: " +date_manip[0]
    print "Day: "+date_manip[1]
    print "Year: "+date_manip[2]

if decide == "n":
        quit()
    
#Decide if they want to continue to next step
decide = raw_input("Would you like to rearrange it into a line? Y/N")

#If they decide yes, execute script otherwise quit
if decide == "y":        
        print ("Month: "+date_manip[0] +
       " Day: "+date_manip[1] +
       " Year: "+date_manip[2])

if decide =="n":
        quit()

#End of script, no matter what they type it will end the program
lastQuestion = raw_input("That's the end, Thank you!")

#If not equal to blank it will quit the program
if lastQuestion != "":
    quit()
    
#if equal to blank it will quit the program
elif lastQuestion == "":
    quit()
