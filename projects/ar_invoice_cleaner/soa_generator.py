undisputed_invoices = [
    {"invoice_no": "INV001", "due_date": "2026-08-01", "amount": 1200},
    {"invoice_no": "INV002", "due_date": "2026-08-15", "amount": 2500},
]

disputed_invoices = [
    {"invoice_no": "INV003", "due_date": "2026-08-10", "amount": 900, "reason": "Pending operational review"},
]

unused_credits = [
    {"credit_no": "CN001", "amount": 500},
]

unallocated_payments = [
    {"payment_ref": "PAY001", "payment_date": "2026-08-20", "amount": 1000},
]

total_undisputed = 0

for invoice in undisputed_invoices:
    total_undisputed += invoice["amount"]

print(total_undisputed)

total_disputed = 0

for invoice in disputed_invoices:
    total_disputed += invoice["amount"]

print(total_disputed)

total_unused_credits = 0

for credit in unused_credits:
    total_unused_credits += credit["amount"]

print(total_unused_credits)


total_unallocated_payments = 0

for payment in unallocated_payments:
    total_unallocated_payments += payment["amount"]

print(total_unallocated_payments)

payment_request = total_undisputed - total_unused_credits - total_unallocated_payments

print(payment_request)

customer_name = "Customer A"


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

soa_text = f"""
Dear {customer_name},

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

print(soa_text)

with open("data/customer_soa.txt", "w") as file:
    file.write(soa_text)

print("Customer SOA has been created: data/customer_soa.txt")