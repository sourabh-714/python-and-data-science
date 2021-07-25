file = open('pic.png','rb')
data = file.read()
file.close()

print(len(data))

# file = open('pic_1.png','wb')
# file.write(data[:100000])
# file.close()
