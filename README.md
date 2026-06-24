# DecodeLab-Internship
# Handwritten Digit Recognition using K-Nearest Neighbors (KNN)

## Project Overview

This project implements a Handwritten Digit Recognition System using the K-Nearest Neighbors (KNN) algorithm from Machine Learning. The model is trained on the Digits dataset provided by Scikit-learn and can classify handwritten digits from 0 to 9.

## Features

* Loads the Digits dataset from Scikit-learn
* Splits data into training and testing sets
* Standardizes features using StandardScaler
* Trains a KNN classifier
* Predicts handwritten digits
* Evaluates model performance using:

  * Accuracy Score
  * Confusion Matrix
  * Classification Report
* Visualizes the Confusion Matrix using Seaborn Heatmap

## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn

## Installation

Install the required libraries:

pip install numpy pandas scikit-learn matplotlib seaborn

## Project Structure

project/
│
├── digit_recognition.py
├── README.md
└── requirements.txt

## How to Run

Run the Python file:

python digit_recognition.py

## Output

The program displays:

1. Training and Testing Dataset Shapes
2. Accuracy Score
3. Confusion Matrix
4. Classification Report
5. Confusion Matrix Visualization

## Machine Learning Workflow

1. Load Dataset
2. Split Dataset
3. Scale Features
4. Train KNN Model
5. Make Predictions
6. Evaluate Performance
7. Visualize Results

## Dataset Information

The Digits dataset contains images of handwritten digits from 0 to 9.

* Total Samples: 1797
* Features per Sample: 64
* Classes: 10 (Digits 0–9)

## Author

Artificial Intelligence Training Project
KNN Based Digit Recognition System
