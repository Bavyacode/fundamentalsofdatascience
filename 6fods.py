import numpy as np
items=5
item_prices = np.array([int(input(f"Enter price of item {i+1}:")) for i in range(items)])
item_quantities = np.array([int(input(f"Enter item{j+1} quantity:")) for j in range (items)])

discount_rate = int(input("Discount"))

tax_rate = int(input("Tax"))


total_cost_before_discounts = sum(price * quantity for price, quantity in zip(item_prices, item_quantities))

total_discount_amount = total_cost_before_discounts * (discount_rate / 100)

total_cost_after_discounts = total_cost_before_discounts - total_discount_amount


total_tax_amount = total_cost_after_discounts * (tax_rate / 100)

final_total_cost = total_cost_after_discounts + total_tax_amount

print("Total Cost before discounts and taxes: $", total_cost_before_discounts)
print("Total Discount Amount: $", total_discount_amount)
print("Total Cost after discounts: $", total_cost_after_discounts)
print("Total Tax Amount: $", total_tax_amount)
print("Final Total Cost including taxes: $", final_total_cost)
