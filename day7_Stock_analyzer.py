prices=[7,1,5,4,2,5]
min_price=prices[0]
max_profit=0
buy_day=0
sell_day=0
temp_buy_day=0
for i in range(1,len(prices)):
    profit=prices[i]-min_price
    if profit>max_profit:
        max_profit=profit
        buy_day=temp_buy_day
        sell_day=i
    if prices[i]<min_price:
        min_price=prices[i]
        temp_buy_day=i
    
print("stock prices:",prices)

if max_profit>0:
    print("buy on day",buy_day,"(price =",prices[buy_day],")")
    print("sell on day",sell_day,"(price =",prices[sell_day],")")
else:
    print("no profit can be made")

print("maximum profit:",max_profit)