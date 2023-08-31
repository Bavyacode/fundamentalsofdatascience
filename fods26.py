import numpy as np
from sklearn.linear_model import LinearRegression

def get_input_features():
    
    area = float(input("Enter the area of the house (in square feet): "))
    num_bedrooms = int(input("Enter the number of bedrooms: "))
    
    return np.array([area, num_bedrooms]).reshape(1, -1)

def main():
    
    data = np.array([[1000, 2, 300000],
                     [1500, 3, 450000],
                     [1200, 2, 350000],
                     [1800, 4, 500000]])

    X = data[:, :-1]  
    y = data[:, -1]   

    
    model = LinearRegression()

    
    model.fit(X, y)

   
    new_house_features = get_input_features()

    
    predicted_price = model.predict(new_house_features)

    print(f"Predicted price for the new house: ${predicted_price[0]:.2f}")

if __name__ == "__main__":
    main()
    '''
Enter the area of the house (in square feet): 1300
Enter the number of bedrooms: 3
Predicted price for the new house: $375000.00

'''

