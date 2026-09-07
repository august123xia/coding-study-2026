## Day 19 Review

Today I practiced Python two pointers, SQL LEFT JOIN, and improved my AR SOA automation project.

Python:
- Practiced Reverse String using two pointers.
- Used left and right pointers to swap characters.
- Learned that chars[left], chars[right] = chars[right], chars[left] can swap two values.
- Practiced Merge Sorted Array simple version.
- Used i and j as pointers for two sorted lists.
- Compared nums1[i] and nums2[j], appended the smaller value, and moved the correct pointer.
- Used remaining while loops to append values when one list still has items left.

SQL:
- Learned LEFT JOIN.
- LEFT JOIN keeps all rows from the left table.
- If the right table has no matching row, the result shows NULL.
- IS NULL is used to find missing matches.
- To find customers with no invoices, LEFT JOIN all invoices and filter invoice_id IS NULL.
- To find customers with no unpaid invoices, LEFT JOIN only unpaid invoices and filter invoice_id IS NULL.
- Conditions in ON control what can be matched.
- Conditions in WHERE filter the final result.

Project:
- Improved the AR SOA generator by reading invoice data from a CSV file.
- Used csv.DictReader to read rows as dictionaries.
- Converted amount from string to integer using int().
- Calculated total undisputed unpaid amount.
- Generated customer-readable invoice lines.
- Created customer_soa_from_csv.txt automatically.