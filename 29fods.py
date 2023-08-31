from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Example feature values
X = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [5.8, 2.6, 4.0, 1.2],
    [6.6, 3.0, 4.4, 1.4],
    [7.3, 2.9, 6.3, 1.8]]
# Example target labels
y = [0, 0, 1, 1, 2]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predict = model.predict(X_test)

print(f"Evaluation metrics for the model:")
print(f"Accuracy: {accuracy_score(y_test, predict):.4f}")
print(f"Precision: {precision_score(y_test, predict, average='weighted'):.4f}")
print(f"Recall: {recall_score(y_test, predict, average='weighted'):.4f}")
print(f"F1-Score: {f1_score(y_test, predict, average='weighted'):.4f}")
'''
Evaluation metrics for the model:
Accuracy: 1.0000
Precision: 1.0000
Recall: 1.0000
F1-Score: 1.0000
'''
