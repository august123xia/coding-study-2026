prices = [7, 1, 5, 3, 6, 4]

def max_profit_brute(prices):
    best_profit = 0

    for i in range(len(prices)):
        buy_price = prices[i]

        for j in range(i+1,len(prices)):
            sell_price = prices[j]
            profit = sell_price - buy_price
            if profit > best_profit:
               best_profit = profit
        
    return best_profit


print(max_profit_brute(prices))  

# Review:
# Brute force means trying all possible buy and sell pairs.
# i is the buying day.
# j is the selling day.
# j starts from i + 1 because we must sell after buying.
# This solution works, but it takes O(n^2) time.