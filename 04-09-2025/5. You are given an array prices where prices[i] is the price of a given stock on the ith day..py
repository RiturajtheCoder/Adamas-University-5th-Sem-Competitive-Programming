def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit
print(maxProfit([7,1,5,3,6,4]))  
print(maxProfit([7,6,4,3,1]))    
