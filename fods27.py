import numpy as np
from sklearn.linear_model import LogisticRegression

def get_input_features():
    
    usage_minutes = float(input("Enter the usage minutes: "))
    contract_duration = float(input("Enter the contract duration (in months): "))
    

    return np.array([usage_minutes, contract_duration]).reshape(1, -1)

def main():
   
    data = np.array([[500, 12, 0],
                     [300, 6, 1],
                     [800, 24, 0],
                     [400, 18, 1]])

    X = data[:, :-1]  
    y = data[:, -1]   
    model = LogisticRegression()

    
    model.fit(X, y)

    
    new_customer_features = get_input_features()

    
    predicted_churn_status = model.predict(new_customer_features)

    if predicted_churn_status[0] == 1:
        print("The new customer is predicted to churn.")
    else:
        print("The new customer is predicted not to churn.")

if __name__ == "__main__":
    main()
