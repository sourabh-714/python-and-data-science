import pymysql

connection = pymysql.connect(host = 'localhost',
                             port = 3306,
                             user = 'root',
                             database = 'onlineshop')

cursor = connection.cursor()
query = "select * from products"
cursor.execute(query)
data = cursor.fetchall()
print(data)
