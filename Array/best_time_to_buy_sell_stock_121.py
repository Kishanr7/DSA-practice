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