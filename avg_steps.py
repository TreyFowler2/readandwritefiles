import csv
import calendar

infile = open('steps.csv','r')
csvfile = csv.reader(infile,delimiter=',')
outfile = open('avg_steps.csv', 'w', newline='')

next(csvfile)
writer = csv.writer(outfile,delimiter=',')
outfile.header = ['Month',' '+'Average Steps Taken']
writer.writerow(outfile.header)

totalsteps=0
month = 1
count = 0

for record in csvfile:
    if int(record[0]) == month:
        count += 1
        totalsteps += int(record[1])
    #runs the sum, else statement needs to yield the average and display data
    else:
        average_steps = round((totalsteps / count), 2)
        month_name = calendar.month_name[int(record[0])]
        data = [month_name, average_steps]
        writer.writerow(data)
        month = int(record[0])
        totalsteps = int(record[1])
        count = 1

outfile.close()
