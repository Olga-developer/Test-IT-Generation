bitcoin_price = int(input("What is Bitcoin price today?"))
print("Bitcoin price today is" " " + str(bitcoin_price))

qty_bitcoin = int(input("How much $ do you have?"))
print("You have " + str(qty_bitcoin) + " " "$")

can_buy = qty_bitcoin / bitcoin_price
can_buy = round(can_buy, 7)
print("You can buy" " " + str(can_buy) + " " "BTC")
