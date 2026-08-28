import pandas as pd

df = pd.read_csv("data/invoices.csv")

df["invoice_date"] =  pd.to_datetime(df["invoice_date"])
df["due_date"] = pd.to_datetime(df["due_date"])


today = pd.to_datetime("2026-08-27")

df["days_overdue"] = (today - df["due_date"]).dt.days

def get_aging_bucket(days):
    if days < 0:
        return "Not due"
    elif days <= 30:
        return "0-30 days"
    elif days <= 60:
        return "31-60 days"
    elif days <= 90:
        return "61-90 days"
    else:
        return "90+ days"
    
df["aging_bucket"] = df["days_overdue"].apply(get_aging_bucket)

print(df)

df.to_csv("data/aging_report.csv", index=False)

print("Aging report has been created: data/aging_report.csv")

unpaid_aging = df[df["status"] == "unpaid"]

unpaid_aging.to_csv("data/unpaid_aging_report.csv", index=False)

print("Unpaid aging report has been created: data/unpaid_aging_report.csv")

unpaid_overdue = df[(df["status"] == "unpaid") & (df["days_overdue"] > 0)]

unpaid_overdue = unpaid_overdue.sort_values("days_overdue", ascending=False)

unpaid_overdue.to_csv("data/overdue_report.csv", index=False)


overdue_summary = unpaid_overdue.groupby("aging_bucket")["amount"].sum().reset_index()

print(overdue_summary)

overdue_summary.to_csv("data/overdue_summary_by_bucket.csv", index=False)

print("Overdue summary by bucket has been created: data/overdue_summary_by_bucket.csv")

print("Overdue report has been created: data/overdue_report.csv")

