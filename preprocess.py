import csv

csvFile = open('movie_titles.csv','r',newline='',encoding='utf-8')
csvReader = csv.reader(csvFile)
print(type(csvReader))
print(csvReader)
csvData = list(csvReader)

print(type(csvData[1][1]))

newData = []
newData.append(csvData[0])
for i in range(1, len(csvData)):
    if csvData[i][1] == 'NULL':
        continue
    if int(csvData[i][0])%24 == 1 and int(csvData[i][1]) >= 1960:
        newData.append(csvData[i])
print(len(newData))
print(newData[1][1])

csvFile2 = open('new.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csvFile2)
writer.writerows(newData)

csvFile.close()
csvFile2.close()