import pandas as pd

def create_customer_summary(customer_name):
    df = pd.read_csv("data/invoices.csv")

    customer_invoices = df[df["customer"]==customer_name]

    total_amount = customer_invoices["amount"].sum()

    print(f"{customer_name} total amount:{total_amount}")

create_customer_summary("Amazon")
create_customer_summary("Google")
create_customer_summary("Dnata")