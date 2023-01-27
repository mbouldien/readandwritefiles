import csv

employees = open('EmployeePay.csv', 'r')

reader = csv.reader(employees, delimiter=',')

print()
print(format('ID', '5') + format('Employee Name', '30') + format('Salary', '11') + format('Bonus Rate', '^12') + format('Total Pay', '^13'))
print('-'*71)

next(reader)

for row in reader:
    id = row[0]
    first_name = row[1]
    last_name = row[2]
    salary = float(row[3])
    bonus_decimal = float(row[4])

    full_name = first_name + ' ' + last_name

    bonus_dollars = salary * bonus_decimal
    total_pay = salary + bonus_dollars
    bonus_percent = bonus_decimal * 100
    
    
    print(format(id, '5') + format(full_name, '30') + format('$' + format(salary, ',.2f'), '11') + format(format(bonus_percent, '.2f') + '%', '^12') + format('$' + format(total_pay, ',.2f'), '>12'))

    input()

employees.close()
