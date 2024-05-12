prices = [1, 2]
buy = prices[0]
maxProfit = 0

for i in range(1, len(prices)):
    if prices[i] < buy:
        buy = prices[i]
    else:
        sell = prices[i]-buy
        if sell > maxProfit:
            maxProfit = sell

        else:
            maxProfit
print(maxProfit)
