import pandas as pd

df = pd.read_csv("data/overdue_report.csv")

customer_summary = df.groupby("customer")["amount"].sum().reset_index()

customer_summary = customer_summary.sort_values("amount", ascending=False)

def get_priority(amount):
    
    if amount >=5000:
        return "High"
    elif amount >= 3000:
        return "Medium"
    else:
        return "Low"
    

customer_summary["priority"] = customer_summary["amount"].apply(get_priority)

customer_summary.to_csv("data/overdue_summary_by_customer.csv", index=False)

print("Overdue summary by customer has been created: data/overdue_summary_by_customer.csv")