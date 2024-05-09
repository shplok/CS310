# Problem Statement: 
#  You are given an array where the ith element 
# is the price of a given stock on day i. If you were only permitted to 
# complete at most one transaction (i.e., buy one and sell one share 
# of the stock), design an algorithm to find the maximum profit.

def max_profit(prices):
    if not prices:
        return 0
    
    # Initialize variables
    min_price = prices[0]  # Initialize the minimum price to the first day's price
    max_profit = 0  # Initialize the maximum profit to zero
    
    # Iterate through the prices
    for price in prices:
        # Update the minimum price if the current price is lower
        min_price = min(min_price, price)
        # Update the maximum profit if selling at the current price gives a higher profit
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print("Maximum Profit:", max_profit(prices))
