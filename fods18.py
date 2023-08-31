import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
data={
"age":[23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
"fat":[9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}
df=pd.DataFrame(data)
print(df)
print("Mean age",np.mean(data['age']))
print("Mean fat",np.mean(data['fat']))
print("Median age",np.median(data['age']))
print("Median fat",np.median(data['fat']))
print("Standard deviation age",np.std(data['age']))
print("Standard deviation fat",np.std(data['fat']))
plt.boxplot(df)
plt.show()
plt.scatter(data['age'],data['fat'])
plt.show()
sm.qqplot(df)   
plt.show()
'''
   age   fat
0    23   9.5
1    23  26.5
2    27   7.8
3    27  17.8
4    39  31.4
5    41  25.9
6    47  27.4
7    49  27.2
8    50  31.2
9    52  34.6
10   54  42.5
11   54  28.8
12   56  33.4
13   57  30.2
14   58  34.1
15   58  32.9
16   60  41.2
17   61  35.7
Mean age 46.44444444444444
Mean fat 28.783333333333335
Median age 51.0
Median fat 30.7
Standard deviation age 12.846193652519204
Standard deviation fat 8.993655170915401

'''
