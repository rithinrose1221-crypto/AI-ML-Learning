import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

data =  pd.read_csv("synthetic_indian_jobs.csv")
print(data.head())
print(data.tail())


data = data.drop(columns = ["company"])
data = data.ffill()
data = data.bfill()
data = data.dropna()

le =  LabelEncoder()
for col in data.columns:
    if data[col].dtype == "object" or data[col].dtype == "str":
        data[col] = LabelEncoder().fit_transform(data[col].astype(str))

x =  data.drop("location",axis = 1)
y = data["location"]

model = LogisticRegression(max_iter=2000)
model.fit(x,y)

Salary = int(input(" Salary(20000=1, 10000=0) :"))
Requirements = int(input ("Requirements(Qulifcation=1, Not = 0):"))
Contact =int(input("Contact(Visit=1, 1Online=0):"))
Archetype =int (input("Archetype(Free fee =1, No fee=0) :"))
Label = int(input ("Label (Yes=1, No=0):"))
Source =int (input("source (Indian=1, Not = 0):"))


input_df =pd.DataFrame([[
    Salary,Requirements,
    Contact,Archetype,Label,Source 
]], columns=x.columns)

prediction = model.predict(input_df)

if prediction[0] == 1:
    print("\n It's a fake job ")
else:
    print("\n No, It's not a fake job")
    
prob = model.predict_proba(input_df)
print("Approval Probability:", prob[0][1])

