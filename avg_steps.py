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
accum = 1

for record in csvfile:
    if int(record[0]) == month:
        count += 1
        totalsteps += int(record[1])

        if int(record[0]) == 12:

            month_name = calendar.month_name[accum]
            average_steps = round(totalsteps / count, 2)
            average_steps = str(average_steps)

            outfile.write(month_name + ', ' + average_steps + '\n')

            break
    #runs the sum, else statement needs to yield the average and display data
    else:
        average_steps = round((totalsteps / count), 2)
        month_name = calendar.month_name[accum]
        data = [month_name, average_steps]
        writer.writerow(data)
        month = int(record[0])
        totalsteps = int(record[1])
        accum += 1
        count = 1

outfile.close()
