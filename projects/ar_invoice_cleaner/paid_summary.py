import pandas as pd

df = pd.read_csv("data/invoices.csv")

paid = df[df["status"]== "paid"]

summary = paid.groupby("customer")["amount"].sum()

summary.to_csv("data/pandas_paid_summary.csv")

print("Paid summary has been created: data/pandas_paid_summary.csv")
