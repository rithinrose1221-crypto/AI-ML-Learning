# import matplotlib.pyplot as plt

# year=[2020,2021,2022,2023]
# student=[11,23,44,12]

# plt.plot(year,student)
# plt.show()


# import matplotlib.pyplot as plt

# year=[2006,2007,2008,2008,2009]
# mark=[990,550,800,450,500]

# plt.plot(year,mark)
# plt.show()

# import matplotlib.pyplot as plt 
# import numpy as np

# year = np.array([2000,2005,2010,2020])
# insta_users = np.array(["10k","25k","35k","46k"])

# x=[1,2,3]
# y=[10,20,30]

# style =  dict(marker="h", markersize=5,linestyle=':',linewidth='1')
# plt.plot(x,y,color='red',**style)

# plt.title('hiii')
# plt.xlabel('year')
# plt.ylabel('followers')
# plt.xticks([1,2,3])
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["AI","IOT","PYTHON","JAVA","HTML"])
# y = np.array([45,67,32,55,20])
# # style = dict(marker="*",markersize=5,linestyle="-",linewidth="1")

# plt.bar(x,y, color="black")
# plt.grid(axis="both",linestyle='-')
# plt.title('STUDENT DATA')
# plt.xlabel('COURSE')
# plt.ylabel('STUDENT')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# course = np.array(["AI","IOT","PYTHON","JAVA","HTML"])
# student = np.array([45,67,32,55,20])
# # style = dict(marker="*",markersize=5,linestyle="-",linewidth="1")

# plt.scatter(student,course)
# plt.title('STUDENT DATA')

# plt.show()

# ----------------------------------------------HISTOGRAM-----------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np

# data = np.random.normal(70,10,100)

# plt.hist(data,bins=10,edgecolor="black")
# plt.show()




# ------------------------------------------------SUBPLOT---------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np

# fig,ax =plt.subplots(3,1)

# ax[0].plot([1,2,3],[2,4,6])
# ax[1].bar([1,2,3],[3,4,5])
# ax[2].bar([1,2,3],[7,3,5])

# plt.show()


# --------------------------------------------------------pd WITH matplotlib-----------------------------------------

# import pandas as pd 
# import matplotlib.pyplot as plt

# df = pd.read_csv("anime.csv")
# rate_count=df["rating"].value_counts()

# plt.bar(rate_count.index,rate_count.values, color="blue")
# plt.show()


# import pandas as pd 
# import matplotlib.pyplot as plt

# df = pd.read_csv("titanic.csv")
# sex_count = df["Sex"].value_counts()

# plt.pie(sex_count.values,labels=sex_count.index, autopct="%1.1f%%")
# plt.show()



# --------------------------------------------------EDA-------------------------------------------

# import pandas as pd 
# import numpy as np
# import matplotlib as plt
# import seaborn as sns

# df = pd.read_csv("titanic.csv")
# df["Age"]=df["Age"].fillna(df["Age"].median())
# df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
# df.drop(columns=["Cabin"],inplace=True)

# print(df.head())
# print(df.info())
# print(df.isnull().sum)
# print(df.describe())
# print(df.describe(include='object'))


# import pandas as pd 
# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns

# df = pd.read_csv("titanic.csv")
# sur_count =df[df["Survived"]==1]
# survival_count = sur_count["Sex"].value_counts()
# plt.pie(survival_count, labels=survival_count.index,autopct="%1.1f%%")
# plt.show()



# iris = sns.load_dataset("iris")
# plt.figure(figsize=(6,4))
# iris["sepal_length"].plot(kind="hist",bins=30)
# plt.title("Sepal Length")
# plt.xlabel("Sepal")

# iris["petal_width"].plot(kind="hist",bins=30)
# plt.title("petal_width")
# plt.xlabel("petal")

# iris["species"].value_counts().plot(kind="bar")
# plt.title("Species Count")
# plt.xlabel("Species Count")

# print(iris.head())
# print(iris.describe())
# print(iris.info())
# plt.show()


# import pandas as pd 
# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns

# data = sns.load_dataset("iris")
# plt.figure(figsize=(6,4))
# plt.scatter(data["sepal_length"], data["petal_length"])
# plt.title("Sepal_Length vs Petal_Length")
# plt.xlabel("Sepal_Length")
# plt.ylabel("Petal_Length")
# plt.show()

# df=pd.read_csv("titanic.csv")
# plt.figure(figsize=(6,4))
# plt.scatter(df["Age"], df["Fare"])
# plt.title("Age vs Fare")
# plt.xlabel("Age")
# plt.ylabel("Fare")
# plt.show()



# import pandas as pd
# import numpy as np


# student = pd.read_csv("student_performance.csv")
# print(student.info())
# print(student.head())
# print(student.describe())




# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

# df =pd.read_csv("HS.csv")
# print("Dataset Preview:")
# print(df.head())

# x =df[['weekly_self_study_hours']]
# y = df[['total_score']]

# X_train, X_test, y_train, y_test = train_test_split(
#     x,y, test_size=0.2, random_state=42
# )

# model = LinearRegression()
# model.fit(X_train,y_train)

# y_pred = model.predict(X_test)

# hours = float(input("Enter study hours (0-10) "))

# print("MSE:", mean_squared_error(y_test, y_pred))
# print("R2 Score:", r2_score(y_test, y_pred))

# input_df = pd.DataFrame([[hours]], columns=['weekly_self_study_hours'])
# prediction = model.predict(input_df)[0][0]
# prediction = round(prediction,2)

# def get_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     elif score >= 50:
#         return "D"
#     else:
#         return "F"
    
# print("Predicted Score:",prediction)
# print("predicted Grade:",get_grade(prediction))



# import pandas as pd 
# import numpy as np 
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

# house = pd.read_csv("house_data.csv")
# print("Data preview")
# print(house.head())

# x = house[['square_feet']]
# y = house[['price']]
# 3
# x_train, x_test, y_train, y_test = train_test_split(
#     x,y, test_size=0.2, random_state=20
# )

# model = LinearRegression()
# model.fit(x_train, y_train)

# y_pred = model.predict(x_test)

# house_price = float(input("Enter your cost: "))

# print("MSE:", mean_squared_error(y_test, y_pred))
# print("R2 Score:", r2_score(y_test, y_pred))

# input_house = pd.DataFrame([[house_price]], columns=['square_feet'])
# prediction = model.predict(input_house)[0][0]
# prediction = round(prediction,2)

# def get_area(price):
#     if price >= 400000:
#         return "High price"
#     elif price >= 350000:
#         return "Medium price"
#     elif price >= 250000:
#         return "Normal price"
#     elif price >= 150000:
#         return "Low price"
#     else:
#         return "Lowest price"
        

# print("Predicted Price:",prediction)
# print("predicted Area:",get_area(prediction))

# import pandas as pd 
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import LabelEncoder


# data = pd.read_csv("loan.csv")
# print(data.head())
# print(data.tail())

# data = data.drop(columns=["Loan_ID"])
# data = data.ffill()
# data = data.bfill()
# data = data.dropna()
# print(data.dtypes)
# le = LabelEncoder()
# for col in data.columns:
#     if data[col].dtype == "object" or data[col].dtype == "str":
#         data[col] = LabelEncoder().fit_transform(data[col].astype(str))
        
# x = data.drop("Loan_Status", axis = 1)
# y = data["Loan_Status"]

# model = LogisticRegression(max_iter = 2000)
# model.fit(x,y)

# Gender = int(input("Gender(Male=1, Female =0):"))
# Married = int(input("Married (Yes=1, No=0): "))
# Dependents = int(input("Dependents (0,1,2,3): "))
# Education = int(input("Education (Graduate=1, Not=0): "))
# Self_Employed = int(input("Self Employed (Yes=1, No=0): "))
# ApplicantIncome = float(input("Applicant Income: "))
# CoapplicantIncome = float(input("Coapplicant Income:"))
# LoanAmount = float(input("Loan Amount: "))
# Loan_Amount_Term = float(input("Loan Term: "))
# Credit_History = int(input("Credit History (1 or 0): "))
# Property_Area = int(input("Property Area (Urban=2, Semi=1, Rural=0): "))



# input_df =pd.DataFrame([[
#     Gender, Married, Dependents, Education, Self_Employed,
#     ApplicantIncome, CoapplicantIncome,LoanAmount, Loan_Amount_Term,
#     Credit_History, Property_Area
# ]], columns=x.columns)

# prediction = model.predict(input_df)

# if prediction[0] == 1:
#     print("\n Yes Loan Approved")
# else:
#     print("\n No Loan Rejected")
    
# prob = model.predict_proba(input_df)
# print("Approval Probability:", prob[0][1])


# import pandas as pd 
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import LabelEncoder

# data =  pd.read_csv("fake_job_dataset.csv")
# print(data.head())
# print(data.tail())


# data = data.drop(columns = ["company"])
# data = data.ffill()
# data = data.bfill()
# data = data.dropna()

# le =  LabelEncoder()
# for col in data.columns:
#     if data[col].dtype == "object" or data[col].dtype == "str":
#         data[col] = LabelEncoder().fit_transform(data[col].astype(str))

# x =  data.drop("location",axis = 1)
# y = data["location"]

# model = LogisticRegression(max_iter=2000)
# model.fit(x,y)

# Salary = int(input(" Salary(20000=1, 10000=0) :"))
# Requirements = int(input ("Requirements(Qulifcation=1, Not = 0):"))
# Contact =int(input("Contact(Visit=1, 1Online=0):"))
# Archetype =int (input("Archetype(Free fee =1, No fee=0) :"))
# Label = int(input ("Label (Yes=1, No=0):"))
# Source =int (input("source (Indian=1, Not = 0):"))


# input_df =pd.DataFrame([[
#     Salary,Requirements,
#     Contact,Archetype,Label,Source 
# ]], columns=x.columns)

# prediction = model.predict(input_df)

# if prediction[0] == 1:
#     print("\n It's a fake job ")
# else:
#     print("\n No, It's not a fake job")
    
# prob = model.predict_proba(input_df)
# print("Approval Probability:", prob[0][1])



