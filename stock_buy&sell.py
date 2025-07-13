def getdata():
    a = []
    n = int(input("enter the size of array: "))
    for i in range(n):
        a.append(int(input(f"enter element {i + 1}: ")))
    return a

def stock_buy_and_sell():
    a = list(getdata())
    min_price = float('inf')
    max_profit = 0
    min_index = 0
    buy_day = 0
    sell_day = 0
    for i in range(len(a)):
        if a[i] < min_price:
            min_price = a[i]
            min_index = i
        elif a[i] - min_price > max_profit:
            max_profit = a[i] - min_price
            buy_day = min_index
            sell_day = i
    
    if max_profit == 0:
        return max_profit
    else: 
        print(f"buy on day {buy_day} at {a[buy_day]}")
        print(f"sold on day {sell_day} at {a[sell_day]}")
        return("profit:", max_profit)



print(stock_buy_and_sell())
    