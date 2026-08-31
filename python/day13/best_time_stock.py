def max_profit(prices):
    min_price = prices[0]
    best_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if  profit > best_profit:
            best_profit = profit

    return best_profit     


print(max_profit([7, 1, 5, 3, 6, 4]))   # 5
print(max_profit([7, 6, 4, 3, 1]))      # 0
print(max_profit([1, 2, 3, 4, 5]))      # 4
print(max_profit([3, 8, 2, 5, 1, 4]))   # 5

# Review:
# min_price stores the lowest price seen so far.
# best_profit stores the highest profit found so far.
# For each price, we update min_price first, then calculate today's profit.
# min_price is not the final answer; it is used to calculate profit.
# best_profit is the final answer.

# Review:
# My first idea was to try every possible buying day,
# then search the future days to find the best selling price.
# That brute-force approach works, but it takes O(n^2) time.
#
# The optimized idea is to reverse the perspective:
# for each day, assume we sell today.
# Then the best buying price must be the lowest price seen so far.
#
# min_price stores the lowest price seen so far.
# best_profit stores the highest profit found so far.
# This allows us to solve the problem in one pass, O(n).