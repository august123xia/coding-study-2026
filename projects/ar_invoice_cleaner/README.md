# Accounts Receivable Aging & Overdue Analytics Automation

## Project Overview

This project automates accounts receivable invoice analysis using Python, Pandas, SQL, and CSV files.

It processes invoice data, calculates overdue days, creates aging buckets, summarizes overdue balances by customer, and validates the results with SQL queries.

## Business Problem

In accounts receivable work, finance teams need to track unpaid invoices, overdue balances, aging buckets, and high-priority customers.

Manual tracking can be time-consuming and error-prone, especially when dealing with multiple customers, invoice disputes, and credit note adjustments.

This project simulates a finance operations workflow and automates the overdue invoice reporting process.

## Technologies Used

- Python
- Pandas
- SQL
- SQLite
- CSV
- Git / GitHub

## Key Features

- Read invoice data from CSV files
- Calculate days overdue based on invoice due dates
- Categorize invoices into aging buckets
- Filter unpaid and overdue invoices
- Summarize overdue balances by customer
- Assign priority levels based on overdue amount
- Validate Pandas-generated results using SQL queries

## Input Data

The input file is:

```text
data/invoices.csv

The dataset includes the following fields:
invoice_id
customer
amount
status
invoice_date
due_date

## Output Files

The project generates the following output files:

```text
data/aging_report.csv
data/unpaid_aging_report.csv
data/overdue_report.csv
data/overdue_summary_by_bucket.csv
data/overdue_summary_by_customer.csv

These files show the invoice aging results, unpaid invoice records, overdue invoice records, overdue balances by aging bucket, and overdue balances by customer.

## SQL Validation

The Pandas-generated overdue customer summary is validated using SQL.

Example SQL query:

```sql
SELECT customer, SUM(amount) AS overdue_total
FROM overdue_report
GROUP BY customer
ORDER BY overdue_total DESC;
```

Expected output:

```text
Dnata   5000
Amazon  3500
Google  1800
```

This confirms that the Pandas-generated overdue customer summary matches the SQL calculation.

## What I Learned

Through this project, I practiced building a small data automation workflow using Python, Pandas, SQL, and GitHub.

Key learning points include:

- Reading and processing CSV data with Pandas
- Creating new calculated columns such as days_overdue
- Applying business logic with Python functions
- Grouping and summarizing data by customer and aging bucket
- Exporting cleaned and summarized data into CSV reports
- Using SQL queries to validate Pandas-generated results
- Managing project files and version control with Git and GitHub

## Future Improvements

Possible future improvements include:

- Add data visualization charts
- Build a Streamlit dashboard
- Add customer-level risk scoring
- Add automated email report generation
- Connect the project to a database instead of CSV files
- Build a customer-facing SOA generator for unpaid invoices, disputed invoices, unused credits, and unallocated payments