## Day 20 Review

Today I increased both practice volume and knowledge volume.

Python:
- Rewrote merge_sorted from a blank file.
- Reviewed the difference between for loop and while loop.
- for loop is useful when iterating through a known sequence.
- while loop is useful when pointers need to move based on conditions.
- Practiced Remove Element.
- Learned the in-place overwrite pattern.
- write_pos means the next position for a value we want to keep.
- nums[:write_pos] shows the valid part of the list.

SQL:
- Reviewed LEFT JOIN.
- Learned COALESCE().
- COALESCE(value, 0) replaces NULL with 0.
- Learned CASE WHEN.
- CASE WHEN creates a calculated category based on conditions.
- Used CASE WHEN to classify customers into High, Medium and Low priority.

Project:
- Upgraded the AR SOA generator to read more data from CSV files.
- Added CSV files for disputed invoices, unused credits and unallocated payments.
- Used csv.DictReader to read each CSV file into a list of dictionaries.
- Converted amount from string to integer.
- Calculated total undisputed amount, total disputed amount, total unused credits and total unallocated payments.
- Calculated payment request as undisputed amount minus unused credits and unallocated payments.
- Generated customer_soa_from_csv_v2.txt automatically.