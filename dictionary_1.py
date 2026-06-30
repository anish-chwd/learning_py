employee_1 = {'id':1, 
              'name':'Mike', 
              'location':'CCU',
              }
print (employee_1['id'])
employee_1['salary'] = 50000
employee_1['bonus'] = 1000
employee_1['location'] = 'BOM'

print(employee_1)

employee_1['total payout'] = employee_1['salary'] + employee_1['bonus']
del employee_1['salary']
del employee_1['bonus']

print(employee_1)