import numpy as np

sales_data = np.array([input("Enter row separated by spaces for product {} sales: ".format(i+1)).split() for i in range(3)], dtype=int)

average_price = np.mean(sales_data)

print("Average price of all products sold in the past month:", average_price)
'''
Enter row separated by spaces for product 1 sales: 4567 5678 7654 
Enter row separated by spaces for product 2 sales: 6789 6543 1234 
Enter row separated by spaces for product 3 sales: 3456 7890 7654
Average price of all products sold in the past month: 5718.333333333333

'''
