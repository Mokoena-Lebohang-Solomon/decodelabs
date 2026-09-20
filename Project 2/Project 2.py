# ================================================================
# PROJECT 2: DATA CLASSIFICATION
# AIGoal - Build a Basic Classification Model
# ================================================================

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ------------------------------------------------
# Simple UI
# ------------------------------------------------

print("=" * 70)
print("|                 DATA CLASSIFICATION                         |")
print("|                  AIGoal - Project 2                          |")
print("=" * 70)

print("\n[1] Loading dataset...")

# Load the built-in Breast Cancer dataset
data = load_breast_cancer()

X = data.data
y = data.target

print("| Dataset loaded successfully!")
print(f"| Number of samples : {X.shape[0]}")
print(f"| Number of features: {X.shape[1]}")
print(f"| Classes           : {list(data.target_names)}")

print("=" * 70)


# ------------------------------------------------
# Understand the dataset
# ------------------------------------------------

print("\n[2] Understanding the dataset")

print("-" * 70)

print("| Target classes:")
for number, name in enumerate(data.target_names):
    print(f"| {number} = {name}")

print("-" * 70)

print("| First 5 samples:")
print(X[:5])

print("=" * 70)


# ------------------------------------------------
# Split dataset
# ------------------------------------------------

print("\n[3] Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("| Training samples:", len(X_train))
print("| Testing samples :", len(X_test))

print("=" * 70)


# ------------------------------------------------
# Scale the data
# ------------------------------------------------

print("\n[4] Preparing the data...")

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("| Feature scaling completed.")

print("=" * 70)


# ------------------------------------------------
# Create classification model
# ------------------------------------------------

print("\n[5] Training classification model...")

model = LogisticRegression(max_iter=5000)

model.fit(X_train_scaled, y_train)

print("| Logistic Regression model trained successfully.")

print("=" * 70)


# ------------------------------------------------
# Make predictions
# ------------------------------------------------

print("\n[6] Testing the model...")

y_pred = model.predict(X_test_scaled)

print("| Predictions completed.")

print("=" * 70)


# ------------------------------------------------
# Evaluate model
# ------------------------------------------------

print("\n[7] MODEL RESULTS")

print("-" * 70)

accuracy = accuracy_score(y_test, y_pred)

print(f"| Accuracy: {accuracy * 100:.2f}%")

print("-" * 70)

print("| Classification Report")
print("-" * 70)

print(
    classification_report(
        y_test,
        y_pred,
        target_names=data.target_names
    )
)

print("-" * 70)

print("| Confusion Matrix")
print("-" * 70)

matrix = confusion_matrix(y_test, y_pred)

print(matrix)

print("=" * 70)


# ------------------------------------------------
# Test a sample
# ------------------------------------------------

print("\n[8] SAMPLE PREDICTION")

print("-" * 70)

sample = X_test[0].reshape(1, -1)

sample_scaled = scaler.transform(sample)

prediction = model.predict(sample_scaled)

prediction_name = data.target_names[prediction[0]]

print("| Model prediction:", prediction_name)

print("-" * 70)

if prediction_name == "malignant":
    print("| Result: The model classified the sample as MALIGNANT.")
else:
    print("| Result: The model classified the sample as BENIGN.")

print("=" * 70)

print("\nProject completed successfully!")
print("===============================================================")