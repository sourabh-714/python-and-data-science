import cgi

form = cgi.FieldStorage()

num_1 = int(form.getvalue('f_num'))
num_2 = int(form.getvalue('s_num'))
result = num_1 + num_2

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Sum is {}</h1>
</body>
</html>
""".format(result))