## Day 11 Review

Today I built an AR aging report using Python and Pandas.

Completed:
- Added `invoice_date` and `due_date` columns to the invoice dataset.
- Converted date strings into datetime values using `pd.to_datetime()`.
- Calculated `days_overdue` using `today - due_date`.
- Used `.dt.days` to extract integer day values from timedelta results.
- Created an aging bucket function with `if / elif / else`.
- Applied the function to the `days_overdue` column using `.apply()`.
- Generated multiple CSV reports:
  - `aging_report.csv`
  - `unpaid_aging_report.csv`
  - `overdue_report.csv`
  - `overdue_summary_by_bucket.csv`

Key concepts:
- A DataFrame represents the whole table.
- `df["column"]` returns a Series.
- `df["new_column"] = ...` creates or updates a column.
- `.apply()` applies a function to each value in a Series.
- `unpaid` does not always mean `overdue`.
- Overdue invoices must satisfy both:
  - `status == "unpaid"`
  - `days_overdue > 0`

Business logic:
- `days_overdue > 0` means overdue.
- `days_overdue < 0` means not due yet.
- Aging buckets help summarize overdue risk by time range.

Output:
- Overdue amount by bucket:
  - 0-30 days: 1800
  - 31-60 days: 3500
  - 61-90 days: 5000