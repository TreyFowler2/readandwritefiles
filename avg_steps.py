from audioop import avg
import csv
from statistics import mean

infile = open('steps.csv','r')
csvfile = csv.reader(infile,delimiter=',')
next(csvfile)

m=0
total=0
a=0


for record in csvfile:
    if int(record[0]) == 1:
        m += 1
        total += int(record[1])
        print(total)
        
avg = round(total/m, 2)

avg = str(avg)

print('January' + ', ' + avg)
