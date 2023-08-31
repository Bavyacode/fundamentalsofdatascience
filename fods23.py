import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)
control_group = np.random.normal(loc=50, scale=10, size=100)
treatment_group = np.random.normal(loc=55, scale=10, size=100)

plt.boxplot([control_group, treatment_group], labels=["Control Group", "Treatment Group"])
plt.ylabel("Values")
plt.title("Box Plot of Control Group vs. Treatment Group")
plt.show()

t_stat, p_value = stats.ttest_ind(control_group, treatment_group)

print("P-value:", p_value)

alpha = 0.05  

if p_value < alpha:
    print("The new treatment has a statistically significant effect compared to the placebo.")
else:
    print("There is no statistically significant effect of the new treatment compared to the placebo.")
'''
P-value: 3.819135262679534e-06
The new treatment has a statistically significant effect compared to the placebo
'''
