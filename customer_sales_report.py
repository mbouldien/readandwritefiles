import csv

sales = open('sales.csv', 'r')
salesreport = open('salesreport.csv', 'w')

reader = csv.reader(sales, delimiter=',')
writer = csv.writer(salesreport, delimiter=',')

prev_cust_id = ''
prev_calc_total = 0

next(reader)
header_row = ['CustomerID', 'Total']
writer.writerow(header_row)

for row in reader:
    cust_id = row[0]
    order_date = row[1]
    ship_date = row[2]
    subtotal = float(row[3])
    tax = float(row[4])
    freight = float(row[5])

    if prev_cust_id == '':
        prev_cust_id = cust_id
    
    new_calc_total = subtotal + tax + freight

    if cust_id != prev_cust_id:
        prev_calc_total = format(prev_calc_total, '.2f')
        new_row = [prev_cust_id, prev_calc_total]
        writer.writerow(new_row)
        prev_calc_total = 0
        calc_total = new_calc_total


    if cust_id == prev_cust_id:
        calc_total = prev_calc_total + new_calc_total

    
    prev_cust_id = cust_id
    prev_calc_total = calc_total

prev_calc_total = format(prev_calc_total, '.2f')
new_row = [prev_cust_id, prev_calc_total]
writer.writerow(new_row)

sales.close()
salesreport.close()