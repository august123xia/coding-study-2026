## Day 13 Review

Today I reviewed Valid Anagram and practiced Best Time to Buy and Sell Stock.

Key concepts:
- Brute force means trying all possible buy and sell pairs.
- The brute force stock solution uses two loops:
  - i is the buying day
  - j is the selling day
  - j starts from i + 1 because selling must happen after buying
- The optimized stock solution uses one loop:
  - min_price stores the lowest price seen so far
  - best_profit stores the highest profit found so far
- range(len(prices)) generates indexes.
- prices[i] gets the price at index i.

SQL validation:
- GROUP BY groups rows by customer.
- SUM(amount) calculates total overdue amount.
- ORDER BY sorts the final result.
- I used SQL to validate the Pandas-generated overdue customer summary.