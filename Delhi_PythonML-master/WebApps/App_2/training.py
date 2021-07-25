import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

df=pd.read_csv('Madedata1.csv')
df['Contact_with_covid_patient'] = df['Contact_with_covid_patient'].str.lower()

gender_lab = LabelEncoder()
gender = gender_lab.fit_transform(df['Gender'])
filename = 'gender_lab.sav'
pickle.dump(gender_lab, open(filename, 'wb'))

severity_lab = LabelEncoder()
severity = severity_lab.fit_transform(df['Severity'])
filename = 'severity_lab.sav'
pickle.dump(severity_lab, open(filename, 'wb'))

contact_lab = LabelEncoder()
contact = contact_lab.fit_transform(df['Contact_with_covid_patient'])
filename = 'contact_lab.sav'
pickle.dump(contact_lab, open(filename, 'wb'))

gender_onehot = OneHotEncoder(sparse=False)
gender = gender_onehot.fit_transform(gender.reshape(-1,1))
filename = 'gender_onehot.sav'
pickle.dump(gender_onehot, open(filename, 'wb'))

severity_onehot = OneHotEncoder(sparse=False)
severity = severity_onehot.fit_transform(severity.reshape(-1,1))
filename = 'severity_onehot.sav'
pickle.dump(severity_onehot, open(filename, 'wb'))

contact_onehot = OneHotEncoder(sparse=False)
contact = contact_onehot.fit_transform(contact.reshape(-1,1))
filename = 'contact_onehot.sav'
pickle.dump(contact_onehot, open(filename, 'wb'))

df_updated = df.drop('Gender',axis=1)
df_updated = df_updated.drop('Severity',axis=1)
df_updated = df_updated.drop('Contact_with_covid_patient',axis=1)

X = df_updated.iloc[:,1:-1].values
y = df['Infected'].values

X = np.c_[X,gender,severity,contact]

scaler = StandardScaler()
X = scaler.fit_transform(X)
filename = 'scaler.sav'
pickle.dump(scaler, open(filename, 'wb'))

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.25)

reg = LogisticRegression()
reg.fit(x_train,y_train)
y_pred = reg.predict(x_test)
filename = 'model.sav'
pickle.dump(reg, open(filename, 'wb'))

# 'Country', 'Age', 'Gender', 'fever', 'Bodypain', 'Runny_nose',
#        'Difficulty_in_breathing', 'Nasal_congestion', 'Sore_throat',
#        'Severity', 'Contact_with_covid_patient', 'Infected'

u_age = 23
u_gender = 'Male'
u_fever = 98
u_bodypain = 0
u_runny_nose = 0
u_breath = 0
u_nasal = 0
u_throat = 0
u_severity = 'Moderate'
u_contact = 'no'

# gender_lab.transform([u_gender])
# gen = gender_onehot.transform([gender_lab.transform([u_gender])])
# sev = severity_onehot.transform([severity_lab.transform([u_severity])])
# cont = contact_onehot.transform([contact_lab.transform([u_contact])])
# test_data = np.array([[u_age,u_fever,u_bodypain,u_runny_nose,u_breath,u_nasal,u_throat]])
# test_x = np.c_[test_data,gen,sev,cont]
# test_x = scaler.transform(test_x)
# pred=reg.predict_proba(test_x)
# reg.predict(test_x)

def is_infected(u_age,u_bodypain,u_breath,u_contact,u_fever,u_gender,u_nasal,u_runny_nose,u_severity,u_throat):
    gender_lab.transform([u_gender])
    gen = gender_onehot.transform([gender_lab.transform([u_gender])])
    sev = severity_onehot.transform([severity_lab.transform([u_severity])])
    cont = contact_onehot.transform([contact_lab.transform([u_contact])])
    test_data = np.array([[u_age,u_fever,u_bodypain,u_runny_nose,u_breath,u_nasal,u_throat]])
    test_x = np.c_[test_data,gen,sev,cont]
    test_x = scaler.transform(test_x)
    pred=reg.predict_proba(test_x)
    acc = max(pred[0])*100
    output = reg.predict(test_x)
    if output[0]==0:
        print("Not infected")
    else:
        print("Infected")
    print("Accuracy:",round(acc,3),"%")

is_infected(u_age,u_bodypain,u_breath,u_contact,u_fever,u_gender,u_nasal,u_runny_nose,u_severity,u_throat)
