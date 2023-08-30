import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

X = np.array([[1, 2], [2, 3], [3, 4], [5, 1], [6, 2], [7, 3]])
y = np.array([0, 0, 0, 1, 1, 1])

def main():
    feature1 = float(input("Enter feature 1: "))
    feature2 = float(input("Enter feature 2: "))

    new_patient_features = np.array([[feature1, feature2]])

    k = int(input("Enter the value of k: "))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    new_patient_features = scaler.transform(new_patient_features)

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    prediction = knn.predict(new_patient_features)

    result = "positive" if prediction[0] == 1 else "negative"

    print(f"The prediction for the new patient is: {result}")

if __name__ == "__main__":
    main()
