# import all important libraries

import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score , confusion_matrix, classification_report

# loading dataset

data = load_digits()
x = data.data
y = data.target

# Traing and test dataset

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("Training Data Shape:", x_train.shape)
print("Testing Data Shape:", x_test.shape)

# Data Scaling

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
print("Number of training samples: ", x_train.shape[0])
print("Features per sample: ", x_train.shape[1])

# Train KNN model

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)

# make prediction
y_pred = knn.predict(x_test)

# Evaluate performance

print("======Accuracy Score=====")
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy score: {accuracy:.4f} ")

print("======Confusion Matrix=====")
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n",cm)

print("====Classification Reort====")
cf = classification_report(y_test, y_pred)
print("Classification Report:\n", cf)


# confusion matrix visulization
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
sns.heatmap(cm,
            annot=True,
            fmt='d',
            cmap='Blues')

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

