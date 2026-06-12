import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    'MonthlyCharge': [50, 80, 70, 40, 90, 60, 100, 85, 45, 75],
    'ContractLength': [12, 6, 24, 12, 3, 18, 24, 6, 12, 18],
    'Age': [30, 25, 40, 35, 28, 50, 45, 32, 29, 55],
    'Churn': [0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
}

df = pd.DataFrame(data)
X = df[['MonthlyCharge', 'ContractLength', 'Age']]
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
