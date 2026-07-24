import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("Employee-attrition.csv")

df.drop(["EmployeeCount", "EmployeeNumber", "Over18", "StandardHours"],
    axis = 1, inplace = True)

encoders = {}

for col in df.select_dtypes(include = "object").columns:
    le = LabelEncoder()
    df[col]= le.fit_transform(df[col])
    encoders[col] = le
    
X = df.drop("Attrition", axis=1)
y = df["Attrition"]

X_train, x_test, y_train, y_test = train_test_split(
    X,y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model. fit(X_train, y_train)

print("InModel Accuracy:", round(model.score(x_test, y_test) * 100, 2),"%")
employee= {}
for col in X.columns:
    employee[col] = X[col].mode()[0] if X[col].dtype == "int64" else X[col] . mean()

print("\n---- Employee Details ----")

employee["Age"] = int(input("Age:"))
employee["MonthlyIncome"] = int(input("Monthly Incone:"))
employee["TotalWorkingYears"] = int(input("Total Working Years:"))
employee["YearsAtCompany"] = int(input("Years at Company: "))

print("\nGender")
print("1. Female")
print("2. Male")
g = int(input("Choose: "))
employee["Gender"] = encoders["Gender"].transform(
    ["Female" if g == 1 else "Male"]
)[0]

print("\nOverTime")
print("1. No")
print("2. Yes")
o = int(input("Choose: "))
employee["OverTime"] = encoders["OverTime"].transform(
    ["No" if o == 1 else "Yes"]
)[0]

print("\nJob Satisfaction")
print("1. Low")
print("2. Medium")
print("3. High")
print("4. Very High")
employee["JobSatisfaction"] = int(input("Choose: "))

input_df = pd.DataFrame([employee])

prediction = model.predict(input_df) [0]
probability = model.predict_proba(input_df) [0]

result = encoders["Attrition"].inverse_transform([prediction])[0]

print("\n========== RESULT ==========")

if result == "Yes":
    print("A Employee is likely to LEAVE the company.")
else:
    print("Employee is likely to STAY in the company.")

print(f"\nStay Probability : {probability[0]*100:.2f}%") 
print(f"Leave Probability: {probability[1]*100:.2f}%")