# Day 9 Review - AR Invoice CSV Cleaner

## What I built today

Today I built AR Invoice CSV Cleaner v0.1.

The project reads invoice data from a CSV file, filters unpaid invoices, summarizes unpaid amount by customer, and outputs a new CSV file.

## Files

- data/invoices.csv
- cleaner.py
- data/unpaid_summary.csv
- pandas_cleaner.py
- data/pandas_unpaid_summary.csv
- README.md

## Pure Python version

I used:

- csv
- open()
- csv.DictReader
- dictionary / HashMap
- csv.writer
- writer.writerow()

The logic is:

1. Read invoices.csv
2. Loop through each row
3. Keep rows where status is unpaid
4. Convert amount to integer
5. Use a dictionary to summarize unpaid amount by customer
6. Write the result to unpaid_summary.csv

## Pandas version

Core code:

```python
df = pd.read_csv("data/invoices.csv")
unpaid = df[df["status"] == "unpaid"]
summary = unpaid.groupby("customer")["amount"].sum()
summary.to_csv("data/pandas_unpaid_summary.csv")


What I understood
df is a Pandas DataFrame.
df["status"] selects the status column.
df["status"] == "unpaid" creates True / False conditions.
df[condition] keeps rows where the condition is True.
groupby("customer") groups rows by customer.
["amount"].sum() calculates total amount for each customer.


What I need to practice

I can understand the code, but I still need practice writing it from scratch.

Tomorrow I should try to create a paid invoice summary by mysel