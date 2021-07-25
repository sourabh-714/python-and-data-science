import io
try:
    file = open('file_1.txt','r')
    data = file.read()
    print(data)
    # file.write("hello world")
except FileNotFoundError:
    file = open('file_1.txt','w')
except io.UnsupportedOperation:
    print("Unsupported operation")
finally:
    print("File closed...")
    file.close()
