# predict.py

import joblib
import pandas as pd

model = joblib.load("model.pkl")

sample = pd.DataFrame({
    "Income":[45000],
    "Debt":[12000],
    "Credit_History":[1],
    "Loan_Amount":[15000]
})

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Creditworthy")
else:
    print("Not Creditworthy")