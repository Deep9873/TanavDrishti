import pandas as pd
import numpy as np 
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, 'data', 'student_mental_health.csv')
MODEL = os.path.join(BASE, 'model', 'model.pkl')


df = pd.read_csv(DATA)
print("Dataset loaded:", df.shape)



features = [
    'sleep_hours', 'study_hours', 'social_media_hours', 'physical_activity_hours', 'attendance_percent', 'academic_pressure', 'financial_stress', 'social_interaction', 'gender'
]

X = df[features]
y = df['risk_level']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

models = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42)
}

best_model, best_acc = None, 0

print("\n------Model Comparison------")
for name, model in models.items():
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"{name}: {acc*100:.2f}%")
    print(classification_report(y_test, model.predict(X_test),      target_names=['Low','Medium','High']))
    if acc > best_acc:
        best_acc = acc
        best_model = model
                         
print(f"\nBest: {type(best_model).__name__} -> {best_acc*100:.2f}%")


joblib.dump({'model': best_model, 'features': features}, MODEL)
print(f"Model saved: {MODEL}")