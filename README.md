# Coding Study 2026

This repository tracks my Python, SQL, and coding interview study from August to December 2026.

## Structure

- python/: Python fundamentals and coding interview practice
- sql/: SQL practice for data analysis
- projects/: resume-ready data and software projects

## Current Topics

### Python
- List, dictionary, set
- Loops and functions
- Two Sum
- Contains Duplicate
- Valid Anagram

### SQL
- SELECT
- FROM
- WHERE
- ORDER BY
- LIMIT
- DISTINCT

## Goal

Prepare for Data Analyst, Data Engineer, and Software Engineer roles.



# AR Invoice CSV Cleaner

This project reads invoice data from a CSV file, filters unpaid invoices, and generates a summary of unpaid amounts by customer.

## Input

`data/invoices.csv`

Columns:

- invoice_id
- customer
- amount
- status

## Output

`data/unpaid_summary.csv`

The output file contains:

- customer
- unpaid_total

## How to run

```bash
python3 cleaner.py

## Update - Day 10

Refactored the invoice summary logic into a reusable Pandas function.

The function can generate customer-level summaries for different invoice statuses, such as paid and unpaid.

Output files:
- data/pandas_paid_summary_v2.csv
- data/pandas_unpaid_summary_v2.csv