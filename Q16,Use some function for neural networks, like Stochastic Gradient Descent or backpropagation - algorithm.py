import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

X = np.array([[5, 2, 80], [3, 1, 70], [7, 3, 90], [2, 1, 65], [6, 2, 85], [4, 1, 75]])
y = np.array([1, 0, 1, 0, 1, 0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MLPClassifier(hidden_layer_sizes=(10,), activation='relu', solver='sgd', max_iter=1000, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Classification Report:")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

sns.set(font_scale=1.4) 
sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', cbar=False, annot_kws={'size': 16})
plt.title('Confusion Matrix for Neural Network Prediction')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()