import numpy as np

sales_data = np.array([input("Enter row separated by spaces for product {} sales: ".format(i+1)).split() for i in range(3)], dtype=int)

average_price = np.mean(sales_data)

print("Average price of all products sold in the past month:", average_price)
