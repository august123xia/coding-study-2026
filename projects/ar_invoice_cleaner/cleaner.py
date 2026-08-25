import csv

summary = {}

with open('data/invoices.csv', "r") as file:
    reader = csv.DictReader(file)


    for row in reader:
        if row["status"] == "unpaid":
            customer = row["customer"]
            amount = int(row["amount"])


            if customer in summary:
                summary[customer] += amount
            else:
                summary[customer] = amount


with open("data/unpaid_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["customer", "unpaid_total"])

    for customer, total_amount in summary.items():
        writer.writerow([customer, total_amount])

print("Unpaid summary has been created: data/unpaid_summary.csv")