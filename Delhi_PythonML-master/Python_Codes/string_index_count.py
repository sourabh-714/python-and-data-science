text = "Hello world, this is python programming"
ch = input("Enter the character : ")
n = text.count(ch)
print("Count",n)
index = 0
for i in range(n):
    current_index = text.index(ch,index)
    index = current_index + 1
    print(current_index)
