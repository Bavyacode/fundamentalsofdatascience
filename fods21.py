import math
from scipy import stats
def calculate_sample_size(confidence_level, precision, population_stddev=None):
   
    z_score = stats.norm.ppf(1 - (1 - confidence_level) / 2)

    if population_stddev:
        sample_size = (z_score ** 2 * population_stddev ** 2) / precision ** 2
    else:
        sample_size = (z_score ** 2) / precision ** 2

    return math.ceil(sample_size)

def main():

    sample_size = int(input("Enter the sample size: "))
    confidence_level = float(input("Enter the confidence level (between 0 and 1): "))
    precision = float(input("Enter the desired level of precision: "))

    
    if confidence_level <= 0 or confidence_level >= 1:
        print("Error: Confidence level must be between 0 and 1.")
        return

    if precision <= 0:
        print("Error: Precision must be greater than 0.")
        return

    
    margin_of_error = (precision / 2) * 100

    required_sample_size = calculate_sample_size(confidence_level, precision)

    print(f"Margin of Error: {margin_of_error:.2f}%")
    print(f"Required Sample Size (at {confidence_level:.0%} confidence level and {precision:.2f} precision): {required_sample_size}")

if __name__ == "__main__":
    main()
'''
Enter the sample size: 5
Enter the confidence level (between 0 and 1): .95
Enter the desired level of precision: .005
Margin of Error: 0.25%
Required Sample Size (at 95% confidence level and 0.01 precision): 153659

'''
