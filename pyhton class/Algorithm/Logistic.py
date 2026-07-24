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





import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv("loan.csv")
print(data.head())
print(data.tail())

data = data.drop(columns=["Loan_ID"])
data = data.ffill()
data = data.bfill()
data = data.dropna()
print(data.dtypes)
le = LabelEncoder()
for col in data.columns:
    if data[col].dtype == "object" or data[col].dtype == "str":
        data[col] = LabelEncoder().fit_transform(data[col].astype(str))
        
x = data.drop("Loan_Status", axis = 1)
y = data["Loan_Status"]

model = LogisticRegression(max_iter = 2000)
model.fit(x,y)

Gender = int(input("Gender(Male=1, Female =0):"))
Married = int(input("Married (Yes=1, No=0): "))
Dependents = int(input("Dependents (0,1,2,3): "))
Education = int(input("Education (Graduate=1, Not=0): "))
Self_Employed = int(input("Self Employed (Yes=1, No=0): "))
ApplicantIncome = float(input("Applicant Income: "))
CoapplicantIncome = float(input("Coapplicant Income:"))
LoanAmount = float(input("Loan Amount: "))
Loan_Amount_Term = float(input("Loan Term: "))
Credit_History = int(input("Credit History (1 or 0): "))
Property_Area = int(input("Property Area (Urban=2, Semi=1, Rural=0): "))



input_df =pd.DataFrame([[
    Gender, Married, Dependents, Education, Self_Employed,
    ApplicantIncome, CoapplicantIncome,LoanAmount, Loan_Amount_Term,
    Credit_History, Property_Area
]], columns=x.columns)

prediction = model.predict(input_df)

if prediction[0] == 1:
    print("\n Yes Loan Approved")
else:
    print("\n No Loan Rejected")
    
prob = model.predict_proba(input_df)
print("Approval Probability:", prob[0][1])