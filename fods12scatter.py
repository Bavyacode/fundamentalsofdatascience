import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall_values = [50, 40, 60, 80, 100, 120, 130, 120, 100, 80, 60, 50]

def create_rainfall_scatter_plot(months, rainfall_values):
    plt.figure(figsize=(10, 6))  

    plt.scatter(months, rainfall_values, marker='o')

    plt.title('Monthly Rainfall Data')
    plt.xlabel('Month')
    plt.ylabel('Rainfall (mm)')
    plt.grid(True)

    plt.show()

create_rainfall_scatter_plot(months, rainfall_values)
