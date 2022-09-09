import csv

#COMMENTS TAKEN OUT USED TO GENERATE BONUS CSV FILE (Just in case if needed)

infile = open('employeepay.csv','r')
csvfile = csv.reader(infile,delimiter=',')

#outfile = open('employee_bonus.csv','w',newline='')

next(csvfile)
#writer = csv.writer(outfile,delimiter= ',')
#header = ["ID", "Employee", "Salary", " Total Pay"]
#writer.writerow(header)

for record in csvfile:
    Pay = int(record[3])
    Bonus = float(record[4])
    EmpID = record[0]
    Employee = record[1] + ' ' + record[2]
    Total_Pay = Pay * Bonus + Pay
    Total_Pay = str(Total_Pay)
    Total_Pay = ' ' + Total_Pay
    #data = [EmpID, Employee, Pay, Total_Pay]
    #writer.writerow(data)

    print('Employee ID:', record[0])
    print('Name:', record[1] + ' ' + record[2])
    print('Salary:', Pay)
    print('Total Pay', Total_Pay)

    input()
