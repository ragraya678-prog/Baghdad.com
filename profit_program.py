buy_price = float(input("Enter wholesale price: "))
sell_price = float(input("Enter selling price: "))
quantity = int(input("Enter quantity: "))

total_cost = buy_price * quantity
total_sales = sell_price * quantity
profit = total_sales - total_cost

print("Total cost:", total_cost)
print("Total sales:", total_sales)
print("Net profit:", profit)
