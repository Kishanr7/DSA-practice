def maxProfit(prices):
    i = 0
    lo = prices[0]
    hi = prices[0]
    profit = 0 
    n = len(prices)
    
    while i < n - 1:
        
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        lo = prices[i]
        
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        hi = prices[i]
        profit += hi - lo
    return profit
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))