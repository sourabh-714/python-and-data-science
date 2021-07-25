# file = open('file_1.txt','r', encoding='latin1')
# file = open('file_1.txt','rb')
# data = file.read()
# print(data.decode())
# file.close()

# with open('file_1.txt', encoding='utf-8') as file:
#     data = file.read()
#     print(data)

file = open('file_1.txt','r', encoding='utf-8')
# data = file.read()

# will read only 10 characters
# data = file.read(10)

# will read one line at a time
# data = file.readline()

# will read all the lines and return them in a list
# data = file.readlines()

# will start reading file from 30th position
file.seek(5)
data = file.read()
print(data)
file.close()
