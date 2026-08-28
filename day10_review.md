## Day 10 Review

Today I refactored the invoice summary logic into a reusable Pandas function.

Key concepts:
- Function parameters allow the same logic to handle different statuses.
- `filtered = df[df["status"] == status]` creates a filtered DataFrame based on the input status.
- `groupby("customer")["amount"].sum()` summarizes invoice amounts by customer.
- `reset_index()` converts the grouped index back into a normal column.
- `to_csv(..., index=False)` exports a clean CSV file without Pandas row numbers.

Output files:
- data/pandas_paid_summary_v2.csv
- data/pandas_unpaid_summary_v2.csv

My understanding:
- pd is the pandas library alias.
- df / paid / summary are pandas objects.
- Object methods like groupby() and to_csv are called directly from the object.