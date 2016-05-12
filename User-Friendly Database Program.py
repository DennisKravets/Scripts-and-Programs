#User friendly database program
import sqlite3

#Connect to Simpsons Database
conn = sqlite3.connect("simpsons.db")

#Clean up presentation of data
def printData(data):
    for row in data:
        print "Id:", row[0]
        print "Name:", row[1]
        print "Gender:", row[2]
        print "Age:", row[3]
        print "Occupation:", row[4], "\n"



def createTable():
    conn.execute("CREATE TABLE if not exists SIMPSON_INFO (\
             ID INTEGER PRIMARY KEY AUTOINCREMENT,\
             NAME TEXT,\
             GENDER TEXT,\
             AGE INT,\
             OCCUPATION TEXT\
             );")

createTable()


#Add a new charecter into the table
def newCharacter():
    print "\nAdding a new character..."
    # Take Inputs
    name = raw_input("Name: ")
    gender = raw_input("Gender: ")
    age = raw_input("Age: ")
    occupation = raw_input("Occupation: ")
    val_str = "'{}', '{}', '{}', '{}'".format(name, gender, age, occupation)
    sql_str = "INSERT INTO SIMPSON_INFO(NAME, GENDER, AGE, OCCUPATION) VALUES ({});".format(val_str)
    #print sql_str
    conn.execute(sql_str)
    conn.commit()
    print "Number of Changes: ", conn.total_changes



#newCharacter()

#View entire table of data
def viewAll():
    # Create SQL String
    sql_str = "SELECT * FROM SIMPSON_INFO"
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    printData (rows)

#viewAll()

def viewDetails():
   print "\nViewing character details"
   #Take name input
   name = raw_input("Enter the character's name: ")
   sql_str = "SELECT * FROM SIMPSON_INFO WHERE NAME = '{}'".format(name)
   cursor = conn.execute(sql_str)
   rows = cursor.fetchall()
   # test to see if there are values in the database
   if len(rows) == 0:
      print "No records found"
   else:
       printData(rows)
        
#viewDetails()

def deleteCharacter():
    print "\nDeleting a character"

    #Take name input
    name = raw_input("Enter the character's name: ")
    sql_str = "SELECT * FROM SIMPSON_INFO WHERE NAME = '{}'".format(name)
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    #ID Number to Change
    change_id = 0
    if len(rows) == 0:
        print "No records found"
        #end of the function
        end
        return
    elif len(rows) == 1:
        print "One record found"
        #select Row
        row = rows[0]
        #select ID
        change_id = rows[0]
        printData(rows)
    else:
        print "More than one record found..."
        printData(rows)
        change_id = raw_input("Type the ID of the character to update: ")
    print "Change ID:", change_id
    delete = raw_input("Confirm character delete (y/n): ")
    if delete == "y":
         sql_str = "DELETE from SIMPSON_INFO where ID = '{}'".format(change_id)
         conn.execute(sql_str)
         conn.commit()
         print "Number of Changes: ", conn.total_changes
                        
#deleteCharacter()

def options():
    # Print out the options
    print "\nWhat would you like to do?"
    print "1. Add a new character"
    print "2. View all characters"
    print "3. Search for a character"
    print "4. Delete a character"
    print "5. Exit"
    
    #Ask user what they would like to do
    response = raw_input("Please enter a number: ")
    if response == "1":
        newCharacter()
    elif response == "2":
        viewAll()
    elif response == "3":
        viewDetails()
    elif response == "4":
        deleteCharacter()
    else:
        print "Exiting the program"
        leaving = raw_input("Are you sure you want to leave? (y/n): ")
        if leaving == "y":
            quit()
        else:
            options()

#options()

def mainLoop():
    in_loop = True
    while in_loop == True:
        options()
        again = raw_input("Would you like to do something else (y/n)?: ")
        #if answer does not equal "y", exit loop
        if again != "y":
            in_loop = False

mainLoop()
