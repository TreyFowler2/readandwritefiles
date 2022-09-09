import csv

infile = open('customers.csv','r')
csvfile = csv.reader(infile,delimiter=',')

outfile = open('customers_country.csv','w',newline = '')

next(csvfile)
writer = csv.writer(outfile)
header = ["Full Name"," Country"]
writer.writerow(header)

count = 1
for record in csvfile:
    full_name = record[1] + ' ' + record[2]
    country = ' '+ record[4]
    data = [full_name , country]
    writer.writerow(data)
    count = count + 1
print('Total:', count)

outfile.close()

#myfile = open('customer_country.csv', 'w')
#ADD HEADER FOR FULL NAME AND COUNTRY