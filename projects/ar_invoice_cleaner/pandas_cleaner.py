import pandas as pd

df = pd.read_csv("data/invoices.csv")

unpaid = df[df["status"] == "unpaid"]

summary = unpaid.groupby("customer")["amount"].sum()

summary.to_csv("data/pandas_unpaid_summary.csv")

print("Pandas unpaid summary has been created: data/pandas_unpaid_summary.csv")