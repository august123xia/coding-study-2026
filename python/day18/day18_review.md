## Day 18 Review

Today I practiced Python two pointers and SQL JOIN.

Python review:
- nums[i] gets the value at index i.
- nums[-1] gets the last value in a list.
- nums[:3] returns the first three values.
- result[-1] can be used to compare the current value with the last saved value.

LeetCode:
- Practiced Valid Palindrome.
- Practiced Two Sum II - Input Array Is Sorted.
- Both problems use the two pointers pattern.
- left starts from the beginning.
- right starts from the end.
- while left < right means the loop continues until the two pointers meet.
- continue skips the rest of the current loop and starts the next loop.
- isalnum() checks whether a character is a letter or number.
- lower() is used to compare characters without caring about uppercase or lowercase.
- In Two Sum II, if total is too small, move left to the right.
- If total is too large, move right to the left.
- The answer uses left + 1 and right + 1 because the problem asks for 1-based indexes.

SQL:
- JOIN connects two tables.
- ON defines the matching condition between two tables.
- invoices.customer_id = customers.customer_id connects invoices with customers.
- WHERE filters original rows.
- AND combines multiple conditions.
- GROUP BY groups rows by a selected column.
- SUM calculates total amount.
- COUNT counts rows.
- HAVING filters grouped results.
- ORDER BY sorts the final result.

Business logic practiced:
- Joined customer information with invoice information.
- Filtered unpaid invoices.
- Calculated unpaid total by customer.
- Calculated unpaid total by country.
- Used HAVING to find customers with unpaid total greater than 3000.