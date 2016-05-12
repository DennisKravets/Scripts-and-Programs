import os, csv
#The path to the script
currentPath = os.path.dirname( \
    os.path.abspath("__file__"))
print currentPath


#make the spreadsheet path
outputCsv = currentPath + '/spreadsheet.csv'
print outputCsv

csvFile = open(outputCsv, "wb")
#csvFile.write("Testing")

#Writing to the file
writer = csv.writer(csvFile, delimiter=",")

#Data to add to the CSV file
row_1 = [1, "Row 1", 123]
row_2 = [2, "Row 2", 456]
row_3 = [3, "Row 3", 789]

#writer.writerow(row_1)
#writer.writerow(row_2)
#writer.writerow(row_3)

rows = [row_1, row_2, row_3]

for row in rows:
    writer.writerow(row)
