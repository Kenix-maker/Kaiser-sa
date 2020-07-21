cash = 10000
money_out = 0
money_in = 0
items = ["eggs", "milk", "bread"]
stocktaking = {"eggs": (0, 0, 0),  "milk": (0, 0, 0), "bread": (0, 0, 0)}

for item in items:
    buying_price = float(input("Enter buying price for {}: ".format(item)))
    selling_price = float(input("Enter selling price for {}: ".format(item)))
    number_of_items = int(input("Enter number of {} you are buying: ".format(item)))
    stocktaking[item] = (buying_price, selling_price, number_of_items)
    money_out += (buying_price * number_of_items)
    money_in += (selling_price * number_of_items)

if money_in > money_out:
    profit = money_in - money_out
    print("You stand to make {} in profit".format(profit))

elif money_in < money_out:
    loses = money_out - money_in
    print("You stand to make {} in loses".format(loses))

else:
    print("You wont make any profit")
