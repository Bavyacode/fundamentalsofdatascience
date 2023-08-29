import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature_values = [25, 26, 27, 28, 29, 30, 31, 30, 29, 28, 27, 26]

def create_temperature_line_plot(months, temperature_values):
    plt.figure(figsize=(10, 6))  

    plt.plot(months, temperature_values, marker='o', linestyle='-')

    plt.title('Monthly Temperature Data')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)

    plt.show()

create_temperature_line_plot(months, temperature_values)
