# Algorithm Explanation:
# Problem: Given an array of stock prices, find the maximum profit you can achieve by buying and selling once.
# Approach:
# 1. Initialize min_price to infinity and max_profit to 0.
# 2. Iterate through each price:
#    - If the current price is less than min_price, update min_price (potential buy).
#    - Else, calculate the profit by selling at the current price and update max_profit if it's higher than previous.
# 3. Return max_profit after checking all prices.

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > max_profit:
            max_profit = p-min_price
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([3,3]))