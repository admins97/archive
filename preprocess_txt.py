import csv

csvFile = open('new.csv','r',newline='',encoding='utf-8')
csvReader = csv.reader(csvFile)
print(type(csvReader))
print(csvReader)
csvData = list(csvReader)

movie_num = []
under_check = False
num = ''
max = 0
for com in csvData:
    if com[0] == 'movie.num':
        continue
    movie_num.append(int(com[0]))


with open("combined_data_4.txt", "r") as f:
    lines = f.readlines()

with open("./new_data_4.txt", "w") as f2:
    for line in lines:
        # print(line[-2])
        # print(line)
        if line[-2] == ':':
            if int(line.split(':')[0]) in movie_num:
                under_check = True
                num = line.split(':')[0] + ','
                max = 0
            else: 
                under_check = False
        else:
            if under_check == True and max < 1000:
                f2.write(num + line)
                max += 1
            else:
                continue
                            
print(len(lines))

# output = open('new_data_1.csv', 'a')    
    

csvFile.close()