def value(name):
    value = 0
    for letter in name:
        value += ord(letter) - 64
    return value

import csv
names = []
with open("names.txt","r") as csvfile:
    csvreader = csv.reader(csvfile)
    names = list(csvreader)[0]

names.sort()

total = 0
for i in range(len(names)):
    name = names[i]
    multiplier = i + 1
    score = multiplier * value(name)
    total += score

print total

