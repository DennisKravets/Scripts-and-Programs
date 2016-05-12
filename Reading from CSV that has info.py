import os, csv
currentPath = os.path.dirname( \
    os.path.abspath("__file__"))
inputCsv = currentPath + "/spreadsheet.csv"

csvFile = open(inputCsv, "rb")
reader = csv.reader(csvFile, delimiter=",")

#print Data from the CSV
#for row in reader:
#    print row
    
readerData = []
for row in reader:
    readerData.append(row)

print readerData
