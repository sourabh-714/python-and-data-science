# modes for write operations - w,a,x
# w - writes the file, if file do not exist then it will create it
# x - writes the file, but it will always create a new file first, if
#     file already exist then it will give error
# a - appends the file instead of overwrite

# file = open('file_2.txt', 'w')
file = open('file_2.txt', 'a')
data = "\nPython file handling is easy to learn"
# data = ["hello","hi","hey"]
file.write(data)
file.close()
