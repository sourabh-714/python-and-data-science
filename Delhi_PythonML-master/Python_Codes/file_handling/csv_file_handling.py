import csv

# data = [
#     ['first name', 'last name', 'salary', 'dept'],
#     ['Raj', 'Kapoor', 35000, 'HR'],
#     ['Rishi','Kapoor',43000, 'IT'],
#     ['Aman','Sharma',47500, 'HR'],
#     ['Kunal','Arora',18000,'IT']
# ]

data = [
    {'name':'Raj Kapoor','salary':45000,'dept':'IT'},
    {'name':'Raj Kumar','salary':42000,'dept':'IT'},
    {'name':'Ajay Singh','salary':35000,'dept':'HR'},
    {'name':'Kunal Sharma','salary':40000,'dept':'HR'},
]

# with open('users.csv','w', newline='') as file:
#     writer = csv.writer(file)
#     for item in data:
#         writer.writerow(item)

with open('users_1.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data[0].keys())
    for i in range(len(data)):
        writer.writerow(data[i].values())
