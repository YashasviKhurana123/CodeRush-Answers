def max_profit(prices):
    # Write your code here
    if len(prices) < 2:
        print(0)  # If there are fewer than 2 prices, no profit can be made.
        return

    min_price = prices[0]  # Initialize the minimum price to the first day's price
    max_profit = 0  # Initialize max profit to zero
    
    for price in prices[1:]:
        # Calculate the profit if we sell at the current price
        profit = price - min_price
        
        # Update the maximum profit if the current profit is higher
        max_profit = max(max_profit, profit)
        
        # Update the minimum price to the lowest seen so far
        min_price = min(min_price, price)
    
    print(max_profit)