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
'''
Enter price of item 1:456
Enter price of item 2:67
Enter price of item 3:900
Enter price of item 4:67
Enter price of item 5:67
Enter item1 quantity:2
Enter item2 quantity:4
Enter item3 quantity:5
Enter item4 quantity:7
Enter item5 quantity:8
Discount6
Tax9
Total Cost before discounts and taxes: $ 6685
Total Discount Amount: $ 401.09999999999997
Total Cost after discounts: $ 6283.9
Total Tax Amount: $ 565.5509999999999
Final Total Cost including taxes: $ 6849.450999999999
'''
