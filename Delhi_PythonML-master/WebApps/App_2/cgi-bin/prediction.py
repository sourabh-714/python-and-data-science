import cgi, pickle
import numpy as np

form = cgi.FieldStorage()

age = form.getvalue('u_age')
gender = form.getvalue('u_gender')
body_temp = form.getvalue('u_temp')
body_pain = form.getvalue('u_pain')
running_nose = form.getvalue('u_nose')
breath_problem = form.getvalue('u_breath')
nasal_congestion = form.getvalue('u_nasal')
sore_throat = form.getvalue('u_throat')
severity_level = form.getvalue('u_severity')
contact = form.getvalue('u_contact')

file = open('gender_lab.sav','rb')
gender_lab = pickle.load(file)
file.close()

file = open('gender_onehot.sav','rb')
gender_onehot = pickle.load(file)
file.close()

file = open('severity_lab.sav','rb')
severity_lab = pickle.load(file)
file.close()

file = open('severity_onehot.sav','rb')
severity_onehot = pickle.load(file)
file.close()

file = open('contact_lab.sav','rb')
contact_lab = pickle.load(file)
file.close()

file = open('contact_onehot.sav','rb')
contact_onehot = pickle.load(file)
file.close()

file = open('scaler.sav', 'rb')
scaler = pickle.load(file)
file.close()

file = open('model.sav', 'rb')
reg = pickle.load(file)
file.close()

gen = gender_onehot.transform([gender_lab.transform([gender])])
sev = severity_onehot.transform([severity_lab.transform([severity_level])])
cont = contact_onehot.transform([contact_lab.transform([contact])])
test_data = np.array([[age,body_temp,body_pain,running_nose,breath_problem,
                       nasal_congestion,sore_throat]])
test_x = np.c_[test_data,gen,sev,cont]

test_x = scaler.transform(test_x)
pred = reg.predict(test_x)

if pred[0] == 0:
    msg = "Not Infected"
else:
    msg = "Infected"

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Prediction is {}</h1>
</body>
</html>
""".format(msg))
