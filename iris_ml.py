from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import load_iris
from sklearn.tree import plot_tree

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

iris = load_iris()

df = pd.DataFrame(
    data=iris.data,
    columns=iris.feature_names
)
df["target"] = iris.target

print(df.head())

sns.pairplot(df, hue="target")
plt.savefig("outputs/pairplot.png")
plt.show()

X = df.drop("target", axis=1)
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", cm)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Tahmin")
plt.ylabel("Gerçek")
plt.title("Confusion Matrix")

plt.savefig("outputs/confusion_matrix.png", bbox_inches="tight")
plt.show()

# Sepal Length, Sepal Width, Petal Length, Petal Width
yeni_cicek = [[5.1, 3.5, 1.4, 0.2]]

tahmin = model.predict(yeni_cicek)
tahmin_ismi = iris.target_names[tahmin[0]]

print(
    f"Bu ölçülere sahip çiçeğin tahmini türü: "
    f"{tahmin_ismi} (Sınıf {tahmin[0]})"
)

importances = model.feature_importances_
feature_names = iris.feature_names

plt.figure(figsize=(8, 5))
sns.barplot(x=importances, y=feature_names)
plt.title("Feature Importance")

plt.savefig("outputs/feature_importance.png", bbox_inches="tight")
plt.show()

plt.figure(figsize=(15, 10))
plot_tree(
    model.estimators_[0],
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True
)

plt.savefig("outputs/decision_tree.png", bbox_inches="tight")
plt.show()
