import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

with open("SMSSpamCollection.csv","r",encoding='latin-1') as f:
    data = [line.strip().split('\t')for line in f]
    
df = pd.DataFrame(data)

df.columns = ["label", "message"]

df["label"] = df ["label"].str.replace('"','',regex=False)

df["label"] = df["label"].map({
    "ham":0,
    "spam":1
})

X = df["message"]
y = df["label"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

print("\nEnter an SMS Message: ")

message = input("Message: ")

message_vector = vectorizer.transform([message])

prediction = model.predict(message_vector)

print("\nPrediction")

if prediction[0] == 1:
    print("Spam Message")
else:
    print("Ham (Normal) Message")
    
