
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# ===========================
# Load Dataset
# ===========================


df = pd.read_csv("adult.csv")

# Rename columns
df.rename(columns={
    "education.num": "education_num",
    "marital.status": "marital_status",
    "capital.gain": "capital_gain",
    "capital.loss": "capital_loss",
    "hours.per.week": "hours_per_week",
    "native.country": "native_country",
    "income": "salary"
}, inplace=True)


# Remove missing values
df.replace("?", pd.NA, inplace=True)
df.dropna(inplace=True)

# ===========================
# Encode Categorical Columns
# ===========================

encoders = {}

categorical_columns = [
    "workclass",
    "education",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native_country",
    "salary"
]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# ===========================
# Train Model
# ===========================

X = df.drop("salary", axis=1)
y = df["salary"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("=" * 45)
print(" EMPLOYEE SALARY PREDICTION SYSTEM ")
print("=" * 45)
print(f"Model Accuracy : {accuracy*100:.2f}%")
print("=" * 45)

# ===========================
# Helper Function
# ===========================

def choose_option(column_name):
    le = encoders[column_name]

    print(f"\nSelect {column_name.upper()}")

    values = list(le.classes_)

    for i, value in enumerate(values):
        print(f"{i} : {value}")

    while True:
        try:
            choice = int(input("Enter choice: "))
            if 0 <= choice < len(values):
                return choice
            else:
                print("Invalid choice.")
        except:
            print("Enter a valid number.")

# ===========================
# User Input
# ===========================

print("\nEnter Employee Details\n")

age = int(input("Age : "))
workclass = choose_option("workclass")
fnlwgt = int(input("Final Weight (fnlwgt): "))
education = choose_option("education")
education_num = int(input("Education Number : "))
marital_status = choose_option("marital_status")
occupation = choose_option("occupation")
relationship = choose_option("relationship")
race = choose_option("race")
sex = choose_option("sex")
capital_gain = int(input("Capital Gain : "))
capital_loss = int(input("Capital Loss : "))
hours_per_week = int(input("Hours Worked Per Week : "))
native_country = choose_option("native_country")

# ===========================
# Prediction
# ===========================

employee = [[
    age,
    workclass,
    fnlwgt,
    education,
    education_num,
    marital_status,
    occupation,
    relationship,
    race,
    sex,
    capital_gain,
    capital_loss,
    hours_per_week,
    native_country
]]

prediction = model.predict(employee)

salary_result = encoders["salary"].inverse_transform(prediction)

print("\n" + "=" * 45)
print("Prediction Result")
print("=" * 45)
print("Predicted Salary :", salary_result[0])
print("=" * 45)