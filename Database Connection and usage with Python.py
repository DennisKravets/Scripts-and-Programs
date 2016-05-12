import sqlite3

#connect to Database "Simpsons.db"
conn = sqlite3.connect("simpsons.db")

# Create the SIMPSON_INFO table with Python
#conn.execute("CREATE TABLE SIMPSON_INFO (\
#             ID INTEGER PRIMARY KEY AUTOINCREMENT,\
#             NAME TEXT,\
#             GENDER TEXT,\
#             AGE INT,\
#             OCCUPATION TEXT\
#             );")

# Insert Bart Simpson into the table
#conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION)\
#       VALUES ('Bart Simpson', 'Male', 10, 'Student')");

# Delete Extra Bart Simpson from the table
#conn.execute("DELETE FROM SIMPSON_INFO WHERE ID = 2")

# Add Homer Simpson into the table
#conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION)\
#       VALUES ('Homer Simpson', 'Male', 40, 'Nuclear Plant')");

#Add Lisa Simpson into the table
#conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION)\
#       VALUES ('Lisa Simpson', 'Female', 8, 'Student')");

# Update SQL with Python
#conn.execute("UPDATE SIMPSON_INFO set AGE=41 WHERE NAME = 'Homer Simpson'")

# DROP DATABASE TABLE
#conn.execute("DROP TABLE SIMPSON_INFO")

#save Changes
#conn.commit()

# Print number of Changes
#changes = conn.total_changes
#print "Number of changes: ", changes

#cursor = conn.execute("SELECT * FROM SIMPSON_INFO")
#rows = cursor.fetchall()
#print rows

