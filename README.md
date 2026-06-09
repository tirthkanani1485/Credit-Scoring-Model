# Credit Scoring Model

## Overview

This project is a Machine Learning-based Credit Scoring Model developed as part of the CodeAlpha Machine Learning Internship. The model predicts whether an individual is creditworthy based on financial information such as income, debt, credit history, and loan amount.

## Objective

To build a classification model that can assess an individual's creditworthiness using historical financial data.

## Features

* Data preprocessing and feature selection
* Creditworthiness prediction using Machine Learning
* Model evaluation using:

  * Accuracy Score
  * Precision
  * Recall
  * F1-Score
  * ROC-AUC Score
  * Confusion Matrix
* Model saving and loading using Joblib

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib

## Project Structure

CodeAlpha_CreditScoring/

├── dataset/

│ └── credit_data.csv

├── train_model.py

├── predict.py

├── model.pkl

├── requirements.txt

└── README.md

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd CodeAlpha_CreditScoring
```

2. Install required packages

```bash
pip install -r requirements.txt
```

## Run Training

```bash
python train_model.py
```

## Run Prediction

```bash
python predict.py
```

## Dataset Features

* Income
* Debt
* Credit_History
* Loan_Amount

Target Variable:

* Creditworthy (1 = Yes, 0 = No)

## Machine Learning Model

Algorithm Used:

* Random Forest Classifier

## Results

The model successfully predicts whether a customer is creditworthy based on financial information and achieves good classification performance on the provided dataset.

## Future Improvements

* Use larger real-world datasets
* Hyperparameter tuning
* Web-based prediction interface using Flask
* Deploy model on cloud platforms

## Internship Task

CodeAlpha Machine Learning Internship

Task 1: Credit Scoring Model

## Author

Tirth Kanani
