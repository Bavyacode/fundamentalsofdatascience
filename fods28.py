import numpy as np
from sklearn.cluster import KMeans

def get_input_features():
    
    num_features = int(input("Enter the number of features: "))
    features = []
    for i in range(num_features):
        feature = float(input(f"Enter feature {i + 1}: "))
        features.append(feature)
    return np.array(features).reshape(1, -1)

def main():
    
    data = np.array([[10, 5],
                     [5, 2],
                     [8, 3],
                     [2, 1]])

    
    num_clusters = 2

    
    kmeans = KMeans(n_clusters=num_clusters)

    
    kmeans.fit(data)

   
    new_customer_features = get_input_features()

   
    predicted_segment = kmeans.predict(new_customer_features)

    print(f"The new customer belongs to segment {predicted_segment[0]}")

if __name__ == "__main__":
    main()
