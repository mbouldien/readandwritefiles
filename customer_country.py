import csv

customers = open('customers.csv','r')
cust_country = open('customer_country.csv', 'w')

reader = csv.reader(customers, delimiter=',')
writer = csv.writer(cust_country, delimiter=',')

i = -1

for row in reader:
    new_row = [row[1], row[2], row[4]]
    writer.writerow(new_row)
    i += 1

print('Number of customers read: ', i)

customers.close()
cust_country.close()