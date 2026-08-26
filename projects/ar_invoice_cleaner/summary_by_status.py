import pandas as pd

def create_summary(status, output_file):
    df = pd.read_csv("data/invoices.csv")

    filtered = df[df["status"] == status]

    summary = filtered.groupby("customer")["amount"].sum().reset_index()

    summary.to_csv(output_file, index=False)

    print(f"{status} summary has been created: {output_file}")


create_summary("paid", "data/pandas_paid_summary_v2.csv")
create_summary("unpaid", "data/pandas_unpaid_summary_v2.csv")