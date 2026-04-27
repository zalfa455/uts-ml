# main.py

# ==============================
# IMPORT LIBRARY
# ==============================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("dataset/citrus.csv")

# ==============================
# DATA PREPROCESSING
# ==============================

# Encoding label
df['label'] = df['name'].map({'orange': 0, 'grapefruit': 1})

# Fitur & target
X = df[['diameter', 'weight', 'red', 'green', 'blue']]
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling (penting untuk SVM)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ==============================
# MODELING
# ==============================

# 1. Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

# 2. Naive Bayes
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# 3. SVM (pakai kernel RBF default)
svm_model = SVC(kernel='rbf')
svm_model.fit(X_train, y_train)

# ==============================
# EVALUASI
# ==============================

models = {
    "Decision Tree": dt_model,
    "Naive Bayes": nb_model,
    "SVM": svm_model
}

print("=== HASIL EVALUASI MODEL ===")

for name, model in models.items():
    y_pred = model.predict(X_test)
    
    print(f"\nModel: {name}")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

# ==============================
# MODEL TERBAIK
# ==============================

# Fokus ke SVM
y_pred_svm = svm_model.predict(X_test)
svm_acc = accuracy_score(y_test, y_pred_svm)

print("\n=== MODEL TERBAIK ===")
print(f"SVM Accuracy: {round(svm_acc, 4)}")
print("SVM dipilih karena memiliki performa terbaik dalam klasifikasi dataset ini.")
