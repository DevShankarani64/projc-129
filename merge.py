import csv

data = []
with open("archive_dataset.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
headers = data[0]
planet_data = data[1:]

#converting all planet names into lower case 
for data_point in planet_data:
    data_point[2]=data_point[2].Lower()
#Sorting planet names into alphabetical order
planet_data.sort(key=lambda planet_data:planet_data[2])

with open ("archive_dataset_sorted.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

#removal of blank lines 
with open ("archive_dataset_sorted.csv","r") as input, open ('archive_dataset_sorted1.csv', 'w', newline = '') as output: 
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(feild.strip() for feild in row):
            writer.writerow(row)