import matplotlib.pyplot as plt

def create_bar_plot(months, sales_values):
    plt.figure(figsize=(10, 6))  

    plt.bar(months, sales_values)

    plt.title('Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Sales Value')
    plt.grid(True)

    plt.show()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_values = [1000, 1500, 1400, 1800, 2000, 1600]
create_bar_plot(months, sales_values)

