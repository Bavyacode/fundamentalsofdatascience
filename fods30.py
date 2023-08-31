import numpy as np
from sklearn.tree import DecisionTreeRegressor, export_text

def load_dataset():
   
    data = np.array([[50000, 2, 1, 0, 20000],
                     [80000, 3, 2, 1, 25000],
                     [60000, 4, 1, 0, 22000],
                     [90000, 3, 3, 1, 30000],
                     [70000, 2, 2, 0, 24000]])

    X = data[:, :-1]  
    y = data[:, -1] 

    return X, y

def get_input_features():
    
    mileage = int(input("Enter the mileage of the car: "))
    age = int(input("Enter the age of the car (in years): "))
    brand = int(input("Enter the brand of the car (0 for Brand A, 1 for Brand B): "))
    engine_type = int(input("Enter the engine type (0 for Gasoline, 1 for Diesel): "))

    return np.array([mileage, age, brand, engine_type]).reshape(1, -1)

def main():
    
    X, y = load_dataset()

    model = DecisionTreeRegressor()

    model.fit(X, y)

    new_car_features = get_input_features()

    predicted_price = model.predict(new_car_features)

    print(f"The predicted price of the new car is ${predicted_price[0]:.2f}")

    tree_rules = export_text(model, feature_names=['Mileage', 'Age', 'Brand', 'Engine Type'])
    print("Decision Path:")
    print(tree_rules)

if __name__ == "__main__":
    main()
    '''
Enter the mileage of the car: 9000
Enter the age of the car (in years): 1
Enter the brand of the car (0 for Brand A, 1 for Brand B): 1
Enter the engine type (0 for Gasoline, 1 for Diesel): 0
The predicted price of the new car is $20000.00
Decision Path:
|--- Mileage <= 85000.00
|   |--- Mileage <= 65000.00
|   |   |--- Age <= 3.00
|   |   |   |--- value: [20000.00]
|   |   |--- Age >  3.00
|   |   |   |--- value: [22000.00]
|   |--- Mileage >  65000.00
|   |   |--- Age <= 2.50
|   |   |   |--- value: [24000.00]
|   |   |--- Age >  2.50
|   |   |   |--- value: [25000.00]
|--- Mileage >  85000.00
|   |--- value: [30000.00]

'''
    
