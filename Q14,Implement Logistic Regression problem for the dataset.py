import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset of student features and labels
# Features: study hours, extracurricular activities, grades
# Labels: 1 for suitable, 0 for not suitable
X = np.array([[5, 2, 80], [3, 1, 70], [7, 3, 90], [2, 1, 65], [6, 2, 85], [4, 1, 75]])
y = np.array([1, 0, 1, 0, 1, 0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

cm = confusion_matrix(y_test, y_pred)

sns.set(font_scale=1.4)  
sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', cbar=False, annot_kws={'size': 16})
plt.title('Confusion Matrix for Problem 14')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
print("Classification Report:")
print(classification_report(y_test, y_pred))
sssssss