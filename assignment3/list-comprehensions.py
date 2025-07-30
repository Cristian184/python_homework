import csv

with open("../csv/employees.csv", newline='') as file:
    reader = list(csv.reader(file))

data = reader[1:]

names = []

for row in data:
    names.append(row[1] + " " + row[2])

print("Names: ", names)

names_with_e = []

for name in names:
    if 'e' in name.lower():
        names_with_e.append(name)

print("Names with 'e':", names_with_e)