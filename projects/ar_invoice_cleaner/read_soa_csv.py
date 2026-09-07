import csv

undisputed_invoices = []

with open("data/soa_undisputed_invoices.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["amount"] = int(row["amount"])
        undisputed_invoices.append(row)


total_undisputed = 0

for invoice in undisputed_invoices:
    total_undisputed += invoice["amount"]


invoice_lines = ""

for invoice in undisputed_invoices:
    invoice_lines += f'{invoice["invoice_no"]} | {invoice["due_date"]} | ${invoice["amount"]:,.2f}\n'

customer_name = "Customer A"

soa_text = f"""
Dear {customer_name},

Please find below the current statement of account summary.

1. Undisputed Unpaid Invoices
Invoice No | Due Date | Amount
{invoice_lines}
Total undisputed unpaid amount: ${total_undisputed:,.2f}

Please arrange payment for the undisputed overdue amount at your earliest convenience.

Kind regards,
AR Team
"""

with open("data/customer_soa_from_csv.txt", "w") as file:
    file.write(soa_text)

print("Customer SOA has been created: data/customer_soa_from_csv.txt")


def read_csv_file(file_path):
    rows = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["amount"] = int(row["amount"])
            rows.append(row)

    return rows

undisputed_invoices = read_csv_file("data/soa_undisputed_invoices.csv")
disputed_invoices = read_csv_file("data/soa_disputed_invoices.csv")
unused_credits = read_csv_file("data/soa_unused_credits.csv")
unallocated_payments = read_csv_file("data/soa_unallocated_payments.csv")

def calculate_total(rows):
    total = 0

    for row in rows:
        total += row["amount"]

    return total


total_undisputed = calculate_total(undisputed_invoices)
total_disputed = calculate_total(disputed_invoices)
total_unused_credits = calculate_total(unused_credits)
total_unallocated_payments = calculate_total(unallocated_payments)


undisputed_lines = ""

for invoice in undisputed_invoices:
    undisputed_lines += f'{invoice["invoice_no"]} | {invoice["due_date"]} | ${invoice["amount"]:,.2f}\n'


disputed_lines = ""

for invoice in disputed_invoices:
    disputed_lines += f'{invoice["invoice_no"]} | {invoice["due_date"]} | ${invoice["amount"]:,.2f} | {invoice["reason"]}\n'


credit_lines = ""

for credit in unused_credits:
    credit_lines += f'{credit["credit_no"]} | ${credit["amount"]:,.2f}\n'


payment_lines = ""

for payment in unallocated_payments:
    payment_lines += f'{payment["payment_ref"]} | {payment["payment_date"]} | ${payment["amount"]:,.2f}\n'

payment_request = total_undisputed - total_unused_credits - total_unallocated_payments


undisputed_lines = ""

for invoice in undisputed_invoices:
    undisputed_lines += f'{invoice["invoice_no"]} | {invoice["due_date"]} | ${invoice["amount"]:,.2f}\n'


disputed_lines = ""

for invoice in disputed_invoices:
    disputed_lines += f'{invoice["invoice_no"]} | {invoice["due_date"]} | ${invoice["amount"]:,.2f} | {invoice["reason"]}\n'


credit_lines = ""

for credit in unused_credits:
    credit_lines += f'{credit["credit_no"]} | ${credit["amount"]:,.2f}\n'


payment_lines = ""

for payment in unallocated_payments:
    payment_lines += f'{payment["payment_ref"]} | {payment["payment_date"]} | ${payment["amount"]:,.2f}\n'


print(undisputed_lines)
print(disputed_lines)
print(credit_lines)
print(payment_lines)

print("Total undisputed:", total_undisputed)
print("Total disputed:", total_disputed)
print("Total unused credits:", total_unused_credits)
print("Total unallocated payments:", total_unallocated_payments)
print("Payment request:", payment_request)

customer_name = "Customer A"

soa_text_v2 = f"""Dear {customer_name},

Please find below the current statement of account summary.

1. Undisputed Unpaid Invoices
Invoice No | Due Date | Amount
{undisputed_lines}
Total undisputed unpaid amount: ${total_undisputed:,.2f}

2. Invoices Under Dispute
Invoice No | Due Date | Amount | Reason
{disputed_lines}
Total disputed amount: ${total_disputed:,.2f}

These disputed invoices are shown for visibility but are not included in the immediate payment request.

3. Unused Credits
Credit No | Amount
{credit_lines}
Total unused credits: ${total_unused_credits:,.2f}

4. Unallocated Payments
Payment Ref | Payment Date | Amount
{payment_lines}
Total unallocated payments: ${total_unallocated_payments:,.2f}

Could you please confirm how the unused credits and unallocated payments should be allocated?

After excluding invoices under dispute, unused credits, and unallocated payments, the current amount requested for payment is: ${payment_request:,.2f}.

Please arrange payment for the undisputed overdue amount at your earliest convenience.

Kind regards,
AR Team
"""

with open("data/customer_soa_from_csv_v2.txt", "w") as file:
    file.write(soa_text_v2)

print("Customer SOA v2 has been created: data/customer_soa_from_csv_v2.txt")