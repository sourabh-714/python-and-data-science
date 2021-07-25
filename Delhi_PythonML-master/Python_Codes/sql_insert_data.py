import pymysql

connection = pymysql.connect(host = 'localhost',
                             port = 3306,
                             user = 'root',
                             database = 'bmplempdb',
                             autocommit = True)

cursor = connection.cursor()
id = 3
name = 'Sahil'
email = 'sahil12@gmail.com'
pwd = '12234'
dept = 'Sales'
desig = 'Head'
sal = 45000

query = "insert into employees values ({}, '{}', '{}', '{}', '{}', '{}', {})".format(id,email,name,pwd, dept, desig, sal)
cursor.execute(query)
